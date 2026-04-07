#!/usr/bin/env bash
set -euxo pipefail


SOURCE_DIR="quartz-site/quartz-4/public/"
PAGES_DIR="../SeminariLabLiLec-pages"
COMMIT_MSG="${1:-Update site}"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "ERROR: source folder not found: $SOURCE_DIR"
  exit 1
fi

if [ ! -e "$PAGES_DIR/.git" ]; then
  echo "ERROR: $PAGES_DIR/.git not found."
  echo "In a git worktree, .git is often a FILE, not a folder."
  echo "Recreate the worktree first."
  exit 1
fi

CURRENT_BRANCH="$(git -C "$PAGES_DIR" branch --show-current)"
if [ "$CURRENT_BRANCH" != "gh-pages" ]; then
  echo "ERROR: target worktree is on branch '$CURRENT_BRANCH', not 'gh-pages'"
  exit 1
fi

echo "==> Syncing $SOURCE_DIR -> $PAGES_DIR"
rsync -av --delete \
  --exclude='.git' \
  --exclude='.git/' \
  --exclude='.nojekyll' \
  "$SOURCE_DIR" "$PAGES_DIR/"

echo "==> Recreating .nojekyll"
touch "$PAGES_DIR/.nojekyll"

echo "==> Git status"
git -C "$PAGES_DIR" status

echo "==> Adding files"
git -C "$PAGES_DIR" add -A

if git -C "$PAGES_DIR" diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

echo "==> Committing"
git -C "$PAGES_DIR" commit -m "$COMMIT_MSG"

echo "==> Pushing to gh-pages"
git -C "$PAGES_DIR" push origin gh-pages

echo "==> Publish completed."
