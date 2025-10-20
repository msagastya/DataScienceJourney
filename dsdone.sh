#!/usr/bin/env bash
# dsdone.sh
# Usage: dsdone.sh "optional short message"
set -euo pipefail

WORKDIR="$HOME/DataScience"
LASTFILE="$WORKDIR/last_done.txt"
LOGFILE="$WORKDIR/dsdone.log"

# Optional commit message suffix
SUFFIX="${1:-}"

cd "$WORKDIR" || { echo "ERROR: cannot cd to $WORKDIR"; exit 1; }

# Ensure it's a git repo
if [ ! -d ".git" ]; then
  echo "ERROR: $WORKDIR is not a git repository."
  exit 1
fi

# Write today's date
TODAY="$(date +%F)"
echo "$TODAY" > "$LASTFILE"

# Prepare commit message
COMMIT_MSG="chore: study update - $TODAY"
if [ -n "$SUFFIX" ]; then
  COMMIT_MSG="$COMMIT_MSG - $SUFFIX"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] dsdone: staging changes..." >> "$LOGFILE"

# Stage changes (respects .gitignore). If you prefer to only add specific folders,
# replace 'git add -A' with e.g. 'git add notebooks/ notes/ day* README.md'
git add -A

# If nothing staged, skip commit/push but still mark done
if git diff --cached --quiet; then
  echo "No changes to commit. Marked done: $TODAY"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] dsdone: no changes to commit." >> "$LOGFILE"
  exit 0
fi

# Commit
git commit -m "$COMMIT_MSG"

# Determine branch (default to main)
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"

# Push
echo "Pushing to origin/$BRANCH..."
if git push origin "$BRANCH"; then
  echo "✅ Marked done: $TODAY and pushed to GitHub (branch: $BRANCH)."
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] dsdone: push successful." >> "$LOGFILE"
  exit 0
else
  echo "⚠️ Marked done locally: $TODAY (push failed — check network / auth)."
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] dsdone: push failed." >> "$LOGFILE"
  exit 1
fi
