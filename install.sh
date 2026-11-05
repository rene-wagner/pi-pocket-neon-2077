#!/usr/bin/env bash
set -euo pipefail

ROOT="${PI_POCKET_DIR:-$HOME/.pi-pocket}"
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="$ROOT/themes/neon-2077"
FILES=(theme.json colors.toml interface.css theme.css)

# Check all sources before changing the installation.
for file in "${FILES[@]}"; do
    if [[ ! -f "$HERE/$file" ]]; then
        printf 'Missing theme file: %s\n' "$HERE/$file" >&2
        exit 1
    fi
done

mkdir -p "$DEST"
# theme.css imports this file. Never install the repository's personal fonts.
if [[ ! -e "$DEST/fonts.css" && ! -L "$DEST/fonts.css" ]]; then
    : > "$DEST/fonts.css"
fi

# Install theme.css last so its imports are present when Pi Pocket reloads it.
for file in "${FILES[@]}"; do
    cp "$HERE/$file" "$DEST/$file"
done

printf 'Installed NEON//2077 at %s\n' "$DEST"
printf 'Pi Pocket: choose NEON//2077 under Appearance → Theme and Appearance → Colors.\n'
printf 'No server restart is required. Existing fonts.css is preserved.\n'
