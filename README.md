# NEON//2077

Ein ruhiges Cyberpunk-HUD für Pi Pocket **0.27.0 oder neuer**, Theme API 1.

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

Die Appearance-Schriftwahl kann zusätzlich `fonts.css` anlegen und dessen
Import voranstellen. Diese Datei wird vom Theme nicht erstellt oder verändert.

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
- Keine zusätzlichen Endlosanimationen, kein Blur, keine externen Ressourcen.

Die vorhandenen Layouts, Touch-Trefferflächen, Safe Areas, Scrollbereiche,
Tool-Zustandsicons und Tastatur-Fokusringe bleiben erhalten. Persönliche
Textgröße, Fonts, Ligaturen, Breite, Sidebar-Breite, Dichte und Bewegung werden
nicht überschrieben. Desktop-Wallpaper bleibt ebenfalls unangetastet.

## Prüfung

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
- Reduzierte Bewegung über Appearance im Browser geprüft; der zusätzliche
  `prefers-reduced-motion`-Selektor wurde auf korrekte Kaskade geprüft.
- Textkontrast auf Navy: Ice White **16,42:1**, Muted Blue **5,82:1**;
  alle verwendeten Syntax-/Status-Akzentfarben mindestens **5,29:1**.

Die Sichtprüfung verwendet eine separate Testansicht, keine Live-Sitzungen.
Es wurden weder Core-Dateien noch App-Daten oder persönliche Einstellungen
verändert. Die Testansicht ersetzt keinen vollständigen Live-App-End-to-End-Test.
