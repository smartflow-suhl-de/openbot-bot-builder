#!/usr/bin/env python3
"""Builds the OpenBot import zip from AGENT.md, skills/ and routines/.

Source of truth are the files in the repo:

- AGENT.md         -> the agent's `description` (text starting at "You are ...")
- skills/<name>/   -> one skill folder per agent (SKILL.md with frontmatter)
- routines/*.txt   -> one routine each; the prompt is the file content

This agent ships without routines, so the routines list below is empty and
the folder may be absent.

The script writes `import/openbot-import.json` (tracked in the repo), builds
`build/openbot-import/` and packs `dist/openbot-bot-builder.zip` from it. The
zip has the manifest at its root, as OpenBot expects.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AGENT_KEY = "bot-builder"
AGENT_NAME = "Bot builder"
AGENT_TITLE = "OpenBot agent architect"
SOURCE_APP = "openbot-share"
EXPORTED_AT = "2026-11-26T00:00:00Z"
TIMEZONE = "Europe/Berlin"

# (routine name, file in routines/, weekday time). Empty: this agent has none.
ROUTINES: list[tuple[str, str, str]] = []

# Limits from OpenBot (packages/contracts/src/ipc-agent-import.ts).
LIMITS = {
    "key": 64,
    "agentName": 80,
    "agentTitle": 120,
    "agentDescription": 2000,
    "agentSkills": 32,
    "agentRoutines": 64,
    "routineName": 80,
    "routineInstruction": 100_000,
    "skillFiles": 200,
}

STAGE = ROOT / "build" / "openbot-import"
ZIP = ROOT / "dist" / "openbot-bot-builder.zip"
MANIFEST = ROOT / "import" / "openbot-import.json"


def fail(message: str) -> None:
    print(f"FEHLER: {message}", file=sys.stderr)
    raise SystemExit(1)


def description() -> str:
    text = (ROOT / "AGENT.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.startswith("You are ")),
        None,
    )
    if start is None:
        fail("AGENT.md hat keinen Text ab 'You are ...'")
    body = "\n".join(lines[start:]).strip()
    if len(body) > LIMITS["agentDescription"]:
        fail(
            f"description ist {len(body)} Zeichen lang, "
            f"erlaubt sind {LIMITS['agentDescription']}"
        )
    return body


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} beginnt nicht mit YAML-Frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} hat kein schließendes '---'")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        name, sep, value = line.partition(":")
        if sep:
            values[name.strip()] = value.strip().strip('"').strip("'")
    return values


def skills() -> list[tuple[str, Path]]:
    found = []
    for folder in sorted((ROOT / "skills").iterdir()):
        if not folder.is_dir():
            continue
        entry = folder / "SKILL.md"
        if not entry.is_file():
            fail(f"skills/{folder.name} hat keine SKILL.md")
        frontmatter = read_frontmatter(entry)
        missing = {"name", "description"} - set(frontmatter)
        if missing:
            fail(f"skills/{folder.name}/SKILL.md: Frontmatter fehlt {sorted(missing)}")
        if frontmatter["name"] != folder.name:
            fail(
                f"skills/{folder.name}: Frontmatter-Name "
                f"'{frontmatter['name']}' passt nicht zum Ordner"
            )
        files = [p for p in folder.rglob("*") if p.is_file()]
        if len(files) > LIMITS["skillFiles"]:
            fail(f"skills/{folder.name} hat {len(files)} Dateien, erlaubt sind {LIMITS['skillFiles']}")
        found.append((folder.name, folder))
    if not found:
        fail("keine Skills unter skills/ gefunden")
    if len(found) > LIMITS["agentSkills"]:
        fail(f"{len(found)} Skills, erlaubt sind {LIMITS['agentSkills']}")
    return found


def routines() -> list[dict]:
    entries = []
    for name, filename, time in ROUTINES:
        path = ROOT / "routines" / filename
        if not path.is_file():
            fail(f"routines/{filename} fehlt")
        instruction = path.read_text(encoding="utf-8").strip()
        if len(instruction) > LIMITS["routineInstruction"]:
            fail(f"routines/{filename} ist zu lang")
        entries.append(
            {
                "name": name,
                "instruction": instruction,
                "active": False,
                "timezone": TIMEZONE,
                "schedule": {"kind": "weekdays", "time": time},
            }
        )
    if len(entries) > LIMITS["agentRoutines"]:
        fail(f"{len(entries)} Routinen, erlaubt sind {LIMITS['agentRoutines']}")
    for entry in entries:
        if len(entry["name"]) > LIMITS["routineName"]:
            fail(f"Routinenname zu lang: {entry['name']}")
    return entries


def manifest() -> dict:
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", AGENT_KEY):
        fail(f"ungültiger Agent-Key: {AGENT_KEY}")
    if len(AGENT_NAME) > LIMITS["agentName"]:
        fail("Agentenname zu lang")
    if len(AGENT_TITLE) > LIMITS["agentTitle"]:
        fail("Agententitel zu lang")

    paths = [f"agents/{AGENT_KEY}/skills/{name}" for name, _ in skills()]
    return {
        "format": "openbot-agent-import",
        "version": 1,
        "source": {"app": SOURCE_APP, "exportedAt": EXPORTED_AT},
        "agents": [
            {
                "key": AGENT_KEY,
                "name": AGENT_NAME,
                "title": AGENT_TITLE,
                "description": description(),
                "avatar": None,
                "skills": paths,
                "routines": routines(),
                "memories": [],
                "files": None,
            }
        ],
        "channels": [],
    }


def stage(payload: dict) -> None:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    (STAGE / "agents" / AGENT_KEY / "skills").mkdir(parents=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(MANIFEST, STAGE / "openbot-import.json")
    for name, folder in skills():
        shutil.copytree(folder, STAGE / "agents" / AGENT_KEY / "skills" / name)


def zipdir() -> None:
    ZIP.parent.mkdir(parents=True, exist_ok=True)
    if ZIP.exists():
        ZIP.unlink()
    entries = sorted(p for p in STAGE.rglob("*") if p.is_file())
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in entries:
            info = zipfile.ZipInfo(
                path.relative_to(STAGE).as_posix(), date_time=(1980, 1, 1, 0, 0, 0)
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> None:
    payload = manifest()
    stage(payload)
    zipdir()
    agent = payload["agents"][0]
    print(f"Manifest: {MANIFEST.relative_to(ROOT)}")
    print(f"Zip:      {ZIP.relative_to(ROOT)} ({ZIP.stat().st_size} Bytes)")
    print(f"Agent:    {agent['name']} ({agent['key']})")
    print(f"Skills:   {len(agent['skills'])}")
    for path in agent["skills"]:
        print(f"          - {path.rsplit('/', 1)[-1]}")
    print(f"Routinen: {len(agent['routines'])}")
    print(f"description: {len(agent['description'])} / {LIMITS['agentDescription']} Zeichen")


if __name__ == "__main__":
    main()
