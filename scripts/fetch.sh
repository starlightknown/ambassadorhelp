#!/usr/bin/env bash
# Snapshot the public Figma Forum pages used by the dashboard.
# Usage: scripts/fetch.sh <output-dir>
set -euo pipefail
OUT=${1:-raw}; mkdir -p "$OUT/help-others" "$OUT/ask-the-community" "$OUT/topics"
UA="Mozilla/5.0 (ambassadorhelp research snapshot)"
for p in $(seq 1 17); do
  curl -sS -A "$UA" "https://forum.figma.com/activity/unanswered?sort=lastActivityAt&page=$p" -o "$OUT/help-others/p$p.html"; sleep 1
done
for p in $(seq 1 12); do
  curl -sS -A "$UA" "https://forum.figma.com/ask-the-community-7?sort=publishedAt&page=$p" -o "$OUT/ask-the-community/p$p.html"; sleep 1
done
