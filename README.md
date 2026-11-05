# NEON//2077

Ein ruhiges Cyberpunk-HUD für Pi Pocket **0.27.0 oder neuer**, Theme API 1.

## Installation und Updates

Im ausgecheckten Repository ausführen:

```bash
bash install.sh
```

Voraussetzungen: Bash und Pi Pocket **0.27.0 oder neuer**. Keine zusätzlichen
Pakete, kein Build und kein `sudo` erforderlich.

Das Script kopiert die Theme-Dateien nach `~/.pi-pocket/themes/neon-2077`.
Wie beim Terminal-Installer lässt sich das Pi-Pocket-Datenverzeichnis mit
`PI_POCKET_DIR` ändern:

```bash
PI_POCKET_DIR="/pfad/zu/pi-pocket-daten" bash install.sh
```

Für Updates den aktuellen Repository-Stand holen und das Script erneut
aufrufen. Dabei werden `theme.json`, `colors.toml`, `interface.css` und
`theme.css` ersetzt; eigene Änderungen an diesen Dateien vorher sichern.
Eine vorhandene `fonts.css` bleibt unverändert. Fehlt sie, legt der Installer
nur einen leeren CSS-Platzhalter für den Import in `theme.css` an, ohne die
persönlichen Schriftwerte aus dem Repository zu übernehmen.

Die Installation wählt das Theme nicht automatisch aus und ändert keine
persönlichen Appearance-Einstellungen. Anschließend wie unten beschrieben
aktivieren. Ein Server-Neustart ist nicht erforderlich.

## Verwenden

In **Appearance → Theme** `NEON//2077` wählen. Für die vorgesehene Farbpalette
auch in **Appearance → Colors** `NEON//2077` wählen. Theme und Farben bleiben
absichtlich unabhängig: Ein späterer Farbwechsel funktioniert weiterhin,
auch mit einer hellen Palette.

Speichern lädt die Theme-Dateien automatisch neu. Ein Server-Neustart ist
nicht erforderlich. Das Theme ändert keine persönlichen Appearance-Werte.

## Dateien

- `theme.json`: Name, Beschreibung, Version und minimale Pocket-Version.
- `colors.toml`: vollständige dunkle Omarchy-Palette mit 16 Terminalfarben.
- `theme.css`: dokumentierte Farb-, Schrift-, Kontur- und Form-Tokens;
  Anpassungen für alternativ gewählte helle Farben.
- `interface.css`: HUD-Details für Navigation, Nachrichten, Tools, Composer,
  Dialoge, Launcher und Panels; responsive und reduzierte Bewegung.
- `install.sh`: Installation und Updates im Pi-Pocket-Datenverzeichnis.

`theme.css` importiert `fonts.css` für persönliche Schriftwerte aus Appearance.
Der Installer legt diese Datei nur dann als CSS-Platzhalter an, wenn sie fehlt.
Vorhandene Schriftwerte bleiben erhalten; die `fonts.css` aus dem Repository
wird nicht installiert.

## Designsprache

- Void Black `#080A12` als Grund, Midnight Navy `#121629` für Karten.
- Electric Cyan `#00F0FF` für aktive Sessions, Fokus und primäre Aktionen.
- Neon Magenta `#FF2DAA` für markante Aktivitätsköpfe, laufende Tools,
  den Modell-Chip, Code-Konturen und stärkeres sekundäres Hover-Feedback.
- Cyber Yellow `#FCEE09` für Logo, Navigations- und Code-Labels sowie
  deutlichere Freigaben und Warnungen. Die HUD-Signallinie zeigt beide Farben.
- Matrix Green `#39FF88` für Erfolg; Rot `#FF647C` für Fehler und Ablehnung.
- Ice White `#EAF7FF` für Text, Muted Blue `#8893AD` für Metadaten.
- Pocket Inter für Fließtext, Pocket Fira Code mit Nerd-Symbol-Fallback für
  Code und technische Informationen; die persönliche Schriftwahl hat Vorrang.
- Schmale Konturen, kleine Radien, segmentierte Titelleiste und dekoratives
  Eckenmotiv. Kein `clip-path` auf Text oder Bedienelementen.
- Sehr schwache Scanlines nur auf der Rail, Grid nur auf dem Home-Screen.
  Keine überlagerten Effekte auf Antworten oder Freigaben.
- Kleine, zustandsgebundene Lichtanimationen statt dauernder Dekoration.
  Keine Hintergrund-Endlosanimationen, kein Blur, keine externen Ressourcen.

Die vorhandenen Layouts, Touch-Trefferflächen, Safe Areas, Scrollbereiche,
Tool-Zustandsicons und Tastatur-Fokusringe bleiben erhalten. Persönliche
Textgröße, Fonts, Ligaturen, Breite, Sidebar-Breite, Dichte und Bewegung werden
nicht überschrieben. Desktop-Wallpaper bleibt ebenfalls unangetastet.

## Bewegung

Das HUD bleibt im Leerlauf ruhig. Drei kleine Effekte zeigen echte Aktivität
oder den Eingabefokus, ohne Texte oder Layout zu bewegen:

- **Datenimpuls:** Ein Lichtimpuls läuft alle **2,4 s** durch die segmentierte
  Signallinie der Titelleiste, solange die aktuelle Unterhaltung arbeitet
  (Denken, Antwort-Streaming oder Kontextkomprimierung). Andere Sessions lösen
  ihn nicht aus. Bei Freigabe-/Antwort-Wartezuständen und Provider-Limits steht
  die Linie still. Sie zeigt Aktivität, keinen prozentualen Fortschritt.
- **Tool-Puls:** Nur die Statusmarke eines laufenden Tools erhält einen sanften
  magentafarbenen Lichtpuls mit **2,2 s** Periodendauer. Statusicon, Spinner und
  Timeline bleiben erhalten. Bei jedem anderen Tool-Zustand endet der Puls.
  Ein tatsächlich weiterlaufendes paralleles Tool pulsiert auch dann, wenn
  ein anderer Aufruf auf Freigabe wartet; die Freigabekarte selbst bleibt ruhig.
- **Neon-Zündung:** Beim Fokussieren des Eingabefelds leuchtet dessen Kontur
  einmal für **240 ms** auf und geht in den ruhigen Fokusrahmen über. Tippen
  oder der Fokuswechsel zwischen enthaltenen Bedienelementen startet den
  Effekt nicht erneut.

Die Aktivitätseffekte wiederholen sich nur, solange ihr Zustand vorliegt.
Antworten, Code und Freigaben erhalten keine bewegten Überlagerungen.
**Appearance → reduzierte Bewegung** und **`prefers-reduced-motion: reduce`**
schalten alle zusätzlichen Animationen und Übergänge ab. Im
**Forced-Colors-Modus** entfallen die dekorativen Effekte ebenfalls; der
Tastaturfokus bleibt sichtbar. Die gewählte Farbpalette gilt auch für die
Animationen, einschließlich heller Alternativfarben.

## Prüfung

Installer-Syntax und isolierte Installationstests (Python 3, Standardbibliothek):

```bash
bash -n install.sh
python3 -m unittest discover -s test -v
```

Die Installationstests verwenden ausschließlich temporäre Verzeichnisse.
Sie prüfen Standard- und eigene Datenpfade, Aufrufe aus anderen Verzeichnissen,
Updates sowie den Erhalt persönlicher Schriftwerte.

Geprüft gegen die installierte Pi-Pocket-Version **0.27.0**:

- Offizieller `readTheme()`-Lader: akzeptiert; Theme-Stylesheets und die
  persönliche `fonts.css`, 33 Farbwerte, 0 externe Assets. JSON und TOML sind gültig.
- Alle verwendeten Tokens und Parts sind in `web/theme-surface.js` aufgeführt;
  keine internen Klassen oder sprachabhängigen Selektoren.
- Chromium akzeptiert alle CSS-Regeln und Deklarationen.
- Isolierte Komponentenansicht mit dem originalen Pi-Pocket-Stylesheet:
  Smartphone, Tablet und Desktop, einschließlich 320 px schmaler Ansichten
  und 1920 px breiter Ansichten. Keine horizontalen Seitenüberläufe.
- Chat, Code, alle 6 Tool-Zustände, Composer-Fokus, Dialoge und Launcher geprüft;
  lange Dialoginhalte bleiben scrollbar.
- Persönliche Schrift-, Größen-, Dichte- und Breitenwerte sowie helle
  Alternativfarben geprüft. Text bis 32 px erzeugt keinen Seitenüberlauf.
- Lichtanimationen in Chromium bei **320, 390, 820, 1280 und 1920 px** geprüft:
  aktive/ruhende Unterhaltung, Aktivität einer anderen Session, Freigabe- und
  Provider-Limit-Wartezustände, alle 6 Tool-Zustände und Composer-Fokus.
  Signal und Tool-Puls stoppen beim Zustandswechsel; Tippen und interne
  Fokuswechsel starten die Neon-Zündung nicht erneut. Keine Layoutbewegung.
- Appearance-Bewegung (`full`, `fluid`, `reduced` und ohne gesetztes Attribut),
  emuliertes **`prefers-reduced-motion: reduce`** und **Forced Colors** geprüft.
  Die zusätzlichen Effekte sind bei reduzierter Bewegung bzw. Forced Colors
  deaktiviert; der statische Fokus bleibt erhalten. Dunkle und helle Farben
  sowie unveränderte Statusicons und Timeline-Maskierung geprüft.
- Textkontrast auf Navy: Ice White **16,42:1**, Muted Blue **5,82:1**;
  alle verwendeten Syntax-/Status-Akzentfarben mindestens **5,29:1**.

Die Sichtprüfung verwendet eine separate Testansicht, keine Live-Sitzungen.
Es wurden weder Core-Dateien noch App-Daten oder persönliche Einstellungen
verändert. Die Testansicht ersetzt keinen vollständigen Live-App-End-to-End-Test.
