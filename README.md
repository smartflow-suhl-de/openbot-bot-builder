# Bot builder für OpenBot

Importierbares Agenten-Paket für einen selbst gehosteten OpenBot-Server: die
Agenten-Beschreibung und zehn Skills als Zip, das OpenBot unter
**Server-Einstellungen → Importieren** einliest.

Ein Agent, ein Zweck: OpenBot-Agenten entwerfen, auditieren und verbessern —
Profil, `AGENTS.md`, Skills, Erinnerungen, Routinen und Delegation. Er liefert
Diagnose, neu geschriebene Instruktionen und Validierungstests; fremde Bots
ändert er nur mit ausdrücklicher Freigabe des Users.

## Herkunft

Der Agent wurde als öffentliche Share-Seite veröffentlicht und am 26.11.2026
von dort übernommen:

- Share-Seite: <https://openbot.run/agents/q0mAYpIXHmcGpR6oIw1rcw>
- Anzeigename: **Bot builder** (Ersteller: „OpenBot user", kein Profilname)
- Umfang der Vorlage: 10 eingebettete Skills, keine Routinen

Die Vorlage war vollständig auf Portugiesisch. Dieses Repo ist die
**englische Fassung**: Beschreibung, Skill-Beschreibungen, Beispiel-Prompts und
alle Skill-Texte wurden übersetzt. Struktur, Nummerierung, Befehle, Pfade und
Regeln bleiben unverändert; übersetzt wurden nur die Sprache und die Namen der
referenzierten Hilfsdateien (z. B. `competencia-profissional.md` →
`professional-competence.md`).

Originaltexte Portugiesisch (Zwischenstand, nicht Teil des Repos):
`/tmp/opencode/a2/` — kann jederzeit neu von der Share-Seite gezogen werden.

Rechte am Text liegen beim Autor; die OpenBot-App selbst steht unter PolyForm
Noncommercial 1.0.0. Nicht als eigenes Produkt ausgeben.

Nicht Teil der Share-Seite und damit auch nicht hier: der private
System-Prompt, Modell-Einstellungen, Gespräche und Workspace-Dateien des
Erstellers.

## Was drin ist

| Pfad | Inhalt |
|---|---|
| `AGENT.md` | die übersetzte Agenten-Beschreibung (Quelle für `description` im Import) |
| `skills/bot-architect/` | Audit- und Erstellungs-Flow für Bots: Recherche der Profession, zwei Bewertungsachsen, Vorher/Nachher-Tests |
| `skills/product-priority-flow/` | kurze Zyklen planen, Lieferungen mit Owner und prüfbaren Kriterien verfolgen, Statusberichte |
| `skills/sdd-product-requirements/` | Anforderungen für Spec-Driven Development: Scope, `REQ`/`NFR`/`AC`, Abnahmekriterien, Traceability |
| `skills/sdd-ux-specification/` | SDD-Anforderungen in implementierbare UI/UX-Specs übersetzen, UX-Abnahme, Review |
| `skills/sdd-technical-delivery/` | technischer Plan, Traceability-Matrix, Implementierung in prüfbaren Scheiben, Validierung |
| `skills/ui-spec-review/` | UI/UX-Specs schreiben und die Implementierung gegen die Spec prüfen |
| `skills/astro-delivery/` | Änderungen an Astro-Sites: Diagnose, minimale Änderung, Build, Preview |
| `skills/security-first-dev/` | Security-first für öffentliche Oberflächen: Abuse/DDoS, Header, Secrets, Dependencies |
| `skills/social-content-calendar/` | Artikel und Ideen in Post-Entwürfe und Redaktionskalender je Netzwerk |
| `skills/voice-calibration/` | Stimm-/Ton-Guide aus echten Texten des Users bauen und anwenden |
| `import/openbot-import.json` | generiertes Manifest des Import-Pakets |
| `dist/openbot-bot-builder.zip` | fertiges Import-Paket |
| `scripts/build-import.py` | baut Manifest und Zip aus den Dateien oben, prüft die Formatgrenzen |
| `scripts/check-import.py` | prüft ein fertiges Zip gegen die Import-Regeln |

Quelle der Wahrheit sind `AGENT.md` und `skills/`. Manifest und Zip werden
daraus gebaut und nicht von Hand gepflegt.

## Fehlende Referenzdateien

`skills/bot-architect/` verweist auf fünf Hilfsdateien unter
`references/` (Profession, Prinzipien, Rubrik, AGENTS.md-Vorlage,
Testprotokoll). Diese Dateien sind **nicht Teil der Share-Seite** und daher
hier nicht enthalten. Der Skill funktioniert ohne sie, verliert aber die
detaillierten Bewertungsraster. Wer sie braucht, muss sie aus dem
ursprünglichen Bot des Autors ziehen oder selbst schreiben.

## Bauen

```bash
./scripts/build-import.sh
./scripts/check-import.py
```

Ergebnis: `dist/openbot-bot-builder.zip` mit `openbot-import.json` und
`agents/bot-builder/skills/…` im Wurzelverzeichnis, so wie OpenBot es
erwartet.

## In OpenBot installieren

Der Import läuft auf dem OpenBot-Rechner, nichts wird hochgeladen.

1. `dist/openbot-bot-builder.zip` auf den Rechner kopieren, auf dem OpenBot
   läuft (oder die Datei dort herunterladen).
2. In OpenBot **Server-Einstellungen → Importieren** öffnen.
3. **Datei wählen…**, das Zip auswählen und den angezeigten Agenten
   „Bot builder" importieren.
4. OpenBot legt eine Kopie an: Instruktionen und die zehn Skills. Nicht
   übernommen werden Gespräche, Erinnerungen, Modell, Provider und
   Workspace-Dateien des Erstellers; Routinen bringt die Vorlage keine mit.

Ein zweiter Import derselben Datei überschreibt die vorhandene Kopie nicht,
sondern legt eine weitere an (bzw. benennt kollidierende Skills um). Vorher
entscheiden, ob die alte Kopie gelöscht werden soll.

### Nach dem Import

1. **Modell und Provider setzen.** Neue Agenten starten sonst leicht auf
   `codex`; ohne ChatGPT-Login scheitert der erste Turn. Für den Anfang
   `provider: opencode` mit einem im Katalog vorhandenen Modell und passendem
   Reasoning-Effort wählen, dazu ein Backup-Modell.
2. **Zugänge freigeben, aber nur die nötigen.** Der Agent liest Bots über
   `openbot.read_agent`/`list_agents` und schreibt nur mit Freigabe. Für
   Audits braucht er Zugriff auf die Agenten-Ordner; GitHub, Tracker oder
   Sentry nur, wenn er auch deren Projekte prüfen soll.
3. **Erstgespräch führen.** Ein echter Auftrag („Auditiere Bot X") ist der
   beste Test: Der Agent soll erst lesen, dann scored, dann eine Vorlage
   liefern — und vor jeder Änderung an einem anderen Bot fragen.
4. **Klein testen.** Erst einen bestehenden Bot auditieren, Backup prüfen
   (`AGENTS.md.bak-YYYYMMDD`), dann eine Änderung anwenden und den
   Vorher/Nachher-Test laufen lassen.
5. **Grenzen bestätigen.** Vollzugriff, Computer Use und Auto-Approve bleiben
   beim User; der Agent darf sie nur empfehlen.

### Ohne Zip installieren

1. Repo in den Workspace des Agenten klonen, z. B. nach
   `Agents/<name>/openbot-bot-builder`.
2. `AGENT.md` als Agenten-Beschreibung einsetzen (Text ab „You are Bot
   builder …"; maximal 2.000 Zeichen).
3. Dem Agenten den Auftrag geben, die zehn Ordner aus `skills/` mit seinen
   lokalen Skill-Werkzeugen (`create_skill`) zu registrieren. Nicht die
   installierten Kopien unter `.agents/skills` von Hand überschreiben.

## Pflege

- Skill-Text ändern: `skills/<name>/SKILL.md` bearbeiten (Frontmatter `name`
  muss zum Ordnernamen passen), dann `./scripts/build-import.sh` und
  `./scripts/check-import.py`.
- Neue Fassung einspielen: neu bauen, importieren, danach erneut testen.
  Keine ungetestete Aktualisierung in einem laufenden Kanal.
- Übersetzung: Fachbegriffe (Spec-Driven Development, Owner, Handoff,
  Fail-closed, Rate Limiting) bleiben englisch; keine Inhalte ergänzen, die
  nicht in der Vorlage stehen.

Grenzen des Formats, die das Skript prüft: Agenten-Beschreibung 2.000
Zeichen, Name 80, Titel 120, 32 Skills je Agent, 64 Routinen, 80 Zeichen
Routinenname, 200 Dateien je Skill-Ordner, keine `.env`-Dateien, Schlüssel
oder verschachtelten Archive im Zip.
