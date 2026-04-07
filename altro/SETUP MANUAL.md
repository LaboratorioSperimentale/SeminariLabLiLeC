# Comprehensive Manual: Building, Structuring, and Publishing a Quartz Site from an Obsidian Vault with Python Automation and GitHub

## 1. Purpose of This Manual

This manual reconstructs the full working architecture for a project in which:

- an **Obsidian vault** is used as the primary authoring environment,
- a **Python layer** performs preprocessing, generation, normalization, and publication-support tasks,
- **Quartz 4** renders the content into a static website,
- **GitHub** is used as the source-control backbone,
- and **GitHub Pages** (or a Pages-oriented publication branch) is used to publish the generated site.

The goal is not to describe a toy setup, but a robust working architecture suitable for a research, seminar, knowledge-base, or digital humanities project.

This document covers:

1. the general architecture,
2. the role of each folder,
3. the content model in Obsidian,
4. the Python preprocessing workflow,
5. Quartz setup and customization,
6. Git and GitHub publication architecture,
7. the operational commands that matter,
8. the main failure points and how to avoid them.

---

## 2. High-Level Architecture

At a strategic level, the system should be understood as a **pipeline**, not as a random accumulation of folders.

The clean mental model is this:

**Authoring layer → Transformation layer → Rendering layer → Publication layer**

### 2.1 Authoring layer
This is the Obsidian vault. It contains the human-maintained markdown notes, metadata, topic logic, and source content.

### 2.2 Transformation layer
This is the Python layer. It is responsible for:

- reading markdown and YAML frontmatter,
- generating derived pages,
- creating topic pages,
- generating intersection pages when needed,
- cleaning old artifacts,
- normalizing links or metadata,
- ensuring the vault is publication-ready.

### 2.3 Rendering layer
This is Quartz 4. It reads the prepared content and renders a static site with navigation, search, theming, layout, and components.

### 2.4 Publication layer
This is Git + GitHub + GitHub Pages. It handles:

- version control,
- collaboration and rollback,
- branch strategy,
- the separation between source repository and published site artifacts,
- deployment.

That is the real architecture. Anything else is implementation detail.

---

## 3. Strategic Design Principles

Before discussing folders or commands, the design principles must be explicit.

### 3.1 Obsidian is the source of truth for content
The markdown files are the canonical human-readable content.

### 3.2 Python is the source of truth for derivation logic
Anything repetitive, structural, generative, or consistency-related should be automated in Python rather than manually maintained.

### 3.3 Quartz is a renderer, not your knowledge model
Quartz should not carry the whole burden of your semantic model. If you force Quartz to behave like your database, you are making the system brittle.

### 3.4 GitHub Pages is a publication target, not the working environment
Do not confuse the source repository with the published website output.

### 3.5 Keep publication artifacts separate from editable source when possible
The generated site is an output. Treat it like a build artifact unless you intentionally choose a simplified one-repo setup.

### 3.6 Hide implementation noise from the public site
Folders such as `_intersezioni`, scripts, templates, development utilities, cache, and local experiments should not appear in user navigation unless explicitly intended.

---

## 4. Recommended Project Folder Architecture

Below is a strong, realistic structure. You asked for a large manual and at least a dozen folders, so here is a serious architecture rather than a minimal one.

```text
seminari-site/
├── content/
│   ├── Index/
│   ├── Topics/
│   │   ├── _intersezioni/
│   │   ├── animali/
│   │   ├── tre/
│   │   └── ...
│   ├── Lista-Seminari/
│   │   ├── en/
│   │   └── it/
│   ├── Tags/
│   ├── Assets/
│   │   ├── images/
│   │   ├── thumbnails/
│   │   ├── pdf/
│   │   └── media/
│   ├── People/
│   ├── Tutorials/
│   ├── Docs/
│   └── Static/
├── quartz-site/
│   └── quartz-4/
│       ├── quartz/
│       │   ├── components/
│       │   ├── styles/
│       │   ├── util/
│       │   ├── plugins/
│       │   └── i18n/
│       ├── public/
│       ├── docs/
│       └── node_modules/
├── python-nonpub/
│   ├── lib/
│   ├── generators/
│   ├── validators/
│   ├── exporters/
│   ├── reports/
│   └── logs/
├── templates-nonpub/
├── tag-index-source-nonpub/
├── scripts/
├── .github/
│   └── workflows/
├── build-nonpub/
├── dist-nonpub/
├── backups-nonpub/
├── tests-nonpub/
├── docs-nonpub/
├── .venv/
├── .obsidian/
└── README-nonpub/
```

This is more than twelve folders because a serious project needs separation of concerns.

---

## 5. Folder-by-Folder Meaning

### 5.1 `content/`
This is the publication-facing content root consumed by Quartz.

This folder should contain markdown notes and only the static assets that are legitimately part of the site content model.

### 5.2 `content/Index/`
Used for index-like notes, landing pages, entry points, or manually curated navigation pages.

### 5.3 `content/Topics/`
Contains topic pages derived from tags or controlled semantic categories.

These are not random tags splattered across the site. They should represent meaningful navigational objects.

### 5.4 `content/Topics/_intersezioni/`
Contains generated intersection pages between topic categories.

Important principle: these pages may exist for navigation logic, but they should usually be hidden from the main sidebar or explorer if they are implementation-detail pages rather than first-class user-facing sections.

### 5.5 `content/Lista-Seminari/`
Contains seminar pages or catalog pages.

If multilingual content exists, keep language segregation explicit rather than mixing files chaotically.

### 5.6 `content/Lista-Seminari/en/` and `content/Lista-Seminari/it/`
Language-specific folders. This prevents collision, duplication confusion, and broken assumptions in scripts.

### 5.7 `content/Tags/`
This can store tag-related helper pages, but in many architectures it should remain controlled and not become a garbage dump of autogenerated tag junk.

### 5.8 `content/Assets/`
Use this for publication assets that belong to the site.

Subfolders should be explicit:
- `images/` for inline images,
- `thumbnails/` for preview cards or video thumbnails,
- `pdf/` for downloadable documents,
- `media/` for other media assets.

### 5.9 `content/People/`
Optional, but useful if authors, speakers, or contributors are modeled as pages.

### 5.10 `content/Tutorials/`
Optional dedicated area for tutorial material.

### 5.11 `content/Docs/`
Optional documentation area for public-facing technical or explanatory pages.

### 5.12 `content/Static/`
A place for pages or static resources not generated dynamically.

### 5.13 `quartz-site/quartz-4/`
The Quartz installation itself.

This is the rendering engine, not the content source.

### 5.14 `python-nonpub/`
All Python tooling that supports the content pipeline.

The `nonpub` suffix is strategically useful because it signals that the folder is not publication-facing content.

### 5.15 `templates-nonpub/`
Reusable markdown or metadata templates.

### 5.16 `tag-index-source-nonpub/`
Useful if the tag/topic system originally came from source definitions, raw exports, or support files that feed generation scripts.

### 5.17 `scripts/`
Shell wrappers, environment setup scripts, rsync commands, helper utilities.

### 5.18 `.github/workflows/`
GitHub Actions definitions for build, test, and deployment.

### 5.19 `build-nonpub/` and `dist-nonpub/`
For temporary or generated outputs that should not pollute the content tree.

### 5.20 `backups-nonpub/`
Manual backup bundles or script-generated backup snapshots.

### 5.21 `tests-nonpub/`
Tests for Python generation logic.

### 5.22 `docs-nonpub/`
Internal documentation that is not part of the public website.

### 5.23 `.venv/`
Python virtual environment.

Do not mix global Python with project Python if you want reliability.

### 5.24 `.obsidian/`
Obsidian local configuration.

Usually not publication content. Decide carefully what to version and what to ignore.

---

## 6. Content Modeling in the Obsidian Vault

This is where most people become sloppy. Do not.

Your vault should not be just “a folder full of markdown files.” It should be a structured content system.

### 6.1 Notes as content objects
Each markdown note should be treated as a content object with:

- a stable path,
- a title,
- YAML frontmatter,
- controlled metadata,
- explicit semantic relationships.

### 6.2 Use YAML frontmatter consistently
For a seminar-like project, frontmatter may include fields such as:

```yaml
---
title: "UD per Corpora L2"
description: "Seminar page about corpora and second-language didactics"
tags:
  - tre
  - uno
  - ob/animali
layout:
  - seminar
seminar-date: 2026-03-30
seminar-title: "UD per Corpora L2"
seminar-description: "A seminar on corpora and L2 teaching"
seminar-author-codekey:
  - abc
seminar-author-affiliation:
  - University of Bologna
seminar-author-affiliation-unibo:
  - yes
seminar-video-title: "Seminar recording"
seminar-video-link: "https://..."
seminar-video-thumbnail-link: "/Assets/thumbnails/ud-corpora-l2.jpg"
seminar-video-length: "2h"
videoLink: "https://..."
videoThumbnail: "/Assets/thumbnails/ud-corpora-l2.jpg"
videoLabel: "Watch seminar"
status: finished
translation:
  - language: en
    link: /Lista-Seminari/en/ud-per-corpora-l2
---
```

The exact fields may vary, but the key requirement is consistency.

### 6.3 Controlled vocabulary over chaos
Do not allow uncontrolled tag entropy.

Bad system:
- `math`
- `mathematics`
- `matematica`
- `algebra`
- `alg`
- `Maths`

That is not a taxonomy. That is negligence.

Use controlled tags or topic codes.

### 6.4 Topic pages are not the same as raw tags
A topic page is a navigational object. A raw hashtag is just a token. Do not confuse them.

A good pattern is:

- markdown notes carry simple tags,
- Python interprets and groups them,
- Python generates topic pages,
- Quartz renders those pages,
- topic pages become navigational assets.

### 6.5 Separate first-level topics from derived intersections
For example:

- `Topics/animali.md`
- `Topics/tre.md`
- `Topics/_intersezioni/animali---tre.md`

This keeps the main navigation clean while preserving richer derived structures.

---

## 7. Recommended Vault Working Rules

### 7.1 Every publishable note should have frontmatter
If a page is part of the site, it should not be metadata-anarchic.

### 7.2 Keep filenames stable
Do not rename files casually after they become linked or generated against.

### 7.3 Avoid putting logic into filenames when frontmatter can carry it better
Filenames should be human-usable and stable, not overloaded with system semantics.

### 7.4 Distinguish source notes from generated notes
If Python generates a note, either put it in a clearly generated area or document that status clearly.

### 7.5 Keep multilingual variants explicit
Do not fake multilingualism through inconsistent suffixes unless your scripts are built for it.

### 7.6 Avoid duplicate semantic pages
A duplicate file in `it/` and `en/` is fine. A duplicate page pretending to be two different canonical objects is not.

---

## 8. Python Layer: Why It Exists

Quartz alone is not enough for a project with semantic generation logic.

Your Python layer exists because you need a deterministic, inspectable transformation step before build.

Typical Python responsibilities include:

- scanning notes,
- parsing YAML,
- normalizing tags,
- creating topic pages,
- generating intersections,
- deduplicating entries,
- checking missing metadata,
- generating index pages,
- validating language variants,
- cleaning obsolete generated files,
- producing reports.

This is exactly the kind of work that should not be done manually.

---

## 9. Suggested Python Internal Structure

Inside `python-nonpub/`, a more disciplined structure helps.

```text
python-nonpub/
├── main.py
├── config.py
├── lib/
│   ├── frontmatter_io.py
│   ├── markdown_utils.py
│   ├── path_utils.py
│   ├── tag_utils.py
│   └── slug_utils.py
├── generators/
│   ├── topic_pages.py
│   ├── intersections.py
│   ├── seminar_indexes.py
│   └── people_pages.py
├── validators/
│   ├── validate_frontmatter.py
│   ├── validate_duplicates.py
│   ├── validate_links.py
│   └── validate_required_fields.py
├── exporters/
│   ├── export_reports.py
│   └── export_csv.py
├── reports/
└── logs/
```

Even if your current script is monolithic, this is the direction a serious project should move toward.

---

## 10. Python Environment Setup

### 10.1 Create the virtual environment
From the project root:

```bash
python3 -m venv .venv
```

### 10.2 Activate it
On Linux/macOS:

```bash
source .venv/bin/activate
```

### 10.3 Upgrade packaging tools
```bash
pip install --upgrade pip setuptools wheel
```

### 10.4 Install dependencies
Typical examples:

```bash
pip install pyyaml python-frontmatter markdown beautifulsoup4 rich typer
```

If your script uses more specialized features, add them explicitly.

### 10.5 Freeze dependencies
```bash
pip freeze > requirements.txt
```

If reproducibility matters, do not leave the dependency state implicit.

---

## 11. Core Python Workflow

A typical production cycle is:

1. Read source notes from `content/`.
2. Parse YAML frontmatter.
3. Identify publishable notes.
4. Normalize tags or topic markers.
5. Generate `Topics/` pages.
6. Generate `_intersezioni/` pages.
7. Rebuild indices.
8. Report duplicates or missing fields.
9. Write generated markdown back into the vault.
10. Hand off to Quartz build.

This means Python acts as a **pre-build stage**.

---

## 12. Python Script Design Recommendations

### 12.1 Separate pure logic from file writing
Compute data structures first. Write files second.

### 12.2 Keep generated pages deterministic
Same inputs should produce same outputs.

### 12.3 Log duplicates explicitly
For example:

```text
DUPLICATO SALTATO: pathA == pathB
```

That is good practice because silent collision is worse than noisy collision.

### 12.4 Validate before writing
Do not spray broken markdown into your content tree.

### 12.5 Keep helper functions defined and testable
A failure such as:

```text
NameError: name 'collect_notes_by_combo' is not defined
```

means the script architecture is weak or refactoring was incomplete.

That is not just a small bug. It signals insufficient modular discipline.

---

## 13. Quartz 4: Role and Setup

Quartz 4 is the static-site engine that turns the content folder into a website.

### 13.1 Quartz is not optional in this architecture
It handles:

- page rendering,
- navigation,
- backlinks,
- search,
- theming,
- layout,
- component logic.

### 13.2 Node requirement matters
You already encountered the key issue: Quartz 4 requires modern Node.

A suitable environment is approximately:

- Node >= 22
- npm >= 10.9.2

If you ignore this, you get build failures and waste time on nonsense.

### 13.3 Using `nvm`
Install and use Node via `nvm` so the project can pin the right version.

Example:

```bash
nvm install 22
nvm use 22
node -v
npm -v
npx -v
```

### 13.4 Install dependencies in Quartz
Inside the Quartz directory:

```bash
cd quartz-site/quartz-4
npm install
```

### 13.5 Local build
```bash
npx quartz build
```

### 13.6 Local build with preview server
```bash
npx quartz build --serve
```

If you get:

```text
npm error could not determine executable to run
```

then usually one of these is wrong:

- you are in the wrong directory,
- dependencies are not installed,
- Node/npm environment is not correctly activated,
- `npx` is resolving incorrectly.

---

## 14. Quartz Working Directory Discipline

This matters more than beginners think.

If Quartz is installed under:

```text
quartz-site/quartz-4/
```

then commands like these must run from there unless explicitly scripted otherwise:

```bash
cd quartz-site/quartz-4
npm install
npx quartz build --serve
```

Running Quartz commands from the wrong level is one of the dumbest and most common self-inflicted errors.

---

## 15. Quartz Content Integration

There are two common patterns:

### Pattern A: Quartz reads the vault content directly
The `content/` folder is positioned exactly where Quartz expects it.

### Pattern B: Python copies or syncs prepared content into Quartz’s expected content path
This is useful when you want stricter separation.

Given your workflow, a direct or semi-direct relation between project `content/` and Quartz content input is reasonable, provided the pathing is stable and scripted.

---

## 16. Quartz Customization Areas

The most relevant customization points are usually:

- `quartz.config.ts`
- `quartz.layout.ts`
- `quartz/components/`
- `quartz/styles/`
- `quartz/util/`

### 16.1 `quartz.config.ts`
Used for global configuration.

### 16.2 `quartz.layout.ts`
Used for page layout composition and component placement.

This is the correct place for some explorer behavior and sidebar composition.

### 16.3 `quartz/components/`
Custom TSX components live here.

Examples relevant to your project:
- `VideoThumbnail.tsx`
- `ResourcesLinkBox.tsx`
- `ResourcesSection.tsx`

### 16.4 `quartz/util/`
Helper functions used by components.

Example:
- `resources.tsx` exporting `collectResources`

### 16.5 `quartz/styles/`
Custom CSS or SCSS styles.

---

## 17. Handling Custom Components Correctly

A recurrent technicality in Quartz customization is import/export correctness.

### 17.1 If a component exists physically but is not exported, it is effectively absent
Example failure:

```text
Import "VideoThumbnail" will always be undefined because there is no matching export in quartz/components/index.ts
```

Fix:

```ts
export { default as VideoThumbnail } from "./VideoThumbnail"
export { default as ResourcesLinkBox } from "./ResourcesLinkBox"
export { default as ResourcesSection } from "./ResourcesSection"
```

### 17.2 If a utility function is not exported, imports will fail
Example failure:

```text
No matching export in quartz/util/resources.tsx for import "collectResources"
```

Fix the export.

### 17.3 Path discipline matters
If import paths are wrong, Quartz build will fail.

Do not improvise path strings casually.

---

## 18. Hiding Internal Folders from the Explorer

This is critical for your `Topics/_intersezioni` design.

You wanted the intersection pages to exist but not pollute the visible sidebar.

That is the right design.

The folder can remain part of the site structure while being excluded from the explorer via `filterFn` in the `Explorer` component configuration.

Conceptually, the logic is:

- show first-level topic pages,
- hide `_intersezioni` and its descendants,
- still allow direct navigation to those pages when linked.

This is exactly how implementation-detail navigation should be handled.

---

## 19. Site Title and Branding

Quartz defaults are not your identity.

If the site still says “Quartz 4,” it means you have not fully taken control of the configuration.

You should explicitly customize:

- site title,
- site description,
- navbar or header text,
- metadata and social preview fields if used.

A public site that still screams “default scaffold” looks unfinished.

---

## 20. Video and Resource Blocks in Pages

Your project includes pages with seminar videos, thumbnails, and resource sections.

This is a good use of structured frontmatter + custom components.

### 20.1 Why not hardcode this manually in each page?
Because it is repetitive, fragile, and inconsistent.

### 20.2 Better approach
- keep fields in frontmatter,
- let components render them,
- use utility functions to collect and normalize resource lists,
- apply shared CSS classes.

### 20.3 Example rendered elements
- thumbnail block with overlay play icon,
- clickable resource header,
- list of PDF or links,
- consistent spacing and icons.

That is exactly the kind of presentational logic Quartz components should own.

---

## 21. Suggested Operational Order of Work

This is the production sequence you should follow.

### Phase 1: Design the content model
Define:
- content types,
- frontmatter schema,
- tag/topic vocabulary,
- multilingual structure,
- generated vs authored pages.

### Phase 2: Structure the Obsidian vault
Create the folder tree and stable conventions.

### Phase 3: Build the Python preprocessing layer
Implement scanning, parsing, generation, validation.

### Phase 4: Install and configure Quartz
Get a plain site building correctly before customizations.

### Phase 5: Integrate content pipeline
Connect Python outputs to Quartz inputs.

### Phase 6: Customize layout and components
Explorer filter, video blocks, resource boxes, site title, topic navigation.

### Phase 7: Test locally
Build repeatedly until the site is deterministic and clean.

### Phase 8: Set up GitHub repository architecture
Source repo, publication branch or Pages strategy.

### Phase 9: Automate deployment
Use a GitHub Action or controlled push workflow.

### Phase 10: Operational hardening
Add backups, validation reports, and cleanup scripts.

This order matters. If you jump straight to GitHub Pages before the local architecture is solid, you are just exporting confusion to the internet.

---

## 22. Git Repository Strategy

There are two sane options.

### Option A: One repository, separate publication branch
- Main branch contains source project.
- Publication branch contains generated site output.

This is often the most practical approach.

### Option B: Two repositories
- Source repository for the project.
- Separate Pages repository for generated site.

This is cleaner in some cases, but slightly more operationally annoying.

For your setup, a **single main repository plus a dedicated Pages publication branch** is a strong compromise.

---

## 23. Suggested Branch Model

Example:

- `main` → source code, Obsidian content, Python, Quartz config
- `gh-pages` → built static site artifact only

This is the classic pattern.

### Why it works
- source remains clean,
- publication is isolated,
- Pages can deploy directly from `gh-pages`,
- site output does not pollute development history.

---

## 24. What Lives in `main`

The `main` branch should contain:

- `content/`
- `python-nonpub/`
- `templates-nonpub/`
- `tag-index-source-nonpub/`
- `quartz-site/`
- scripts and helper tooling
- project documentation

It should **not** contain your generated site output unless you deliberately choose a simplified architecture.

---

## 25. What Lives in `gh-pages`

The `gh-pages` branch should contain only what is needed to serve the site.

Typically:

- HTML,
- CSS,
- JS,
- static assets,
- `.nojekyll` if needed.

It should **not** carry the entire source tree, virtual environment, Python scripts, or development junk.

---

## 26. Why `.nojekyll` Matters

GitHub Pages can otherwise apply Jekyll processing behavior that interferes with directories beginning with underscores.

Quartz sites commonly use `.nojekyll` to ensure Pages serves the site as-is.

Do not delete it casually.

---

## 27. Manual Publication Workflow

If you want a straightforward manual workflow, the cycle is:

1. Work on `main`.
2. Run Python preprocessing.
3. Build Quartz.
4. Sync the generated output into a local checkout/worktree of `gh-pages`.
5. Commit and push `gh-pages`.

This is explicit and reliable.

---

## 28. Using a Worktree for `gh-pages`

A worktree is often the cleanest way to manage the publication branch locally.

### 28.1 Create it
From the source repo:

```bash
git worktree add ../SeminariLabLiLeC-pages gh-pages
```

If the branch does not exist yet:

```bash
git worktree add -b gh-pages ../SeminariLabLiLeC-pages
```

This creates a second checked-out directory linked to the same repository.

### 28.2 Why it is useful
- `main` stays open in one folder,
- `gh-pages` lives in another folder,
- no repeated branch switching in the same directory,
- easier rsync-based publication.

This is operationally superior to clumsy manual branch hopping.

---

## 29. Important Git Commands for Branch and Worktree Management

### 29.1 See worktrees
```bash
git worktree list
```

### 29.2 Show current branch
```bash
git branch --show-current
```

### 29.3 Check current branch in another directory
```bash
git -C ../SeminariLabLiLeC-pages branch --show-current
```

If this fails with “not a git repository,” the directory is wrong or the worktree was not created correctly.

---

## 30. Publishing with `rsync`

This is one of the cleanest ways to move the built site into the publication branch.

Suppose Quartz build output is in a folder like `public/`.

You often want to sync the built content into the `gh-pages` worktree while preserving `.git` and possibly `.nojekyll`.

### 30.1 Typical safe rsync pattern
```bash
rsync -av --delete \
  --exclude='.git' \
  --exclude='.nojekyll' \
  quartz-site/quartz-4/public/ ../SeminariLabLiLeC-pages/
```

This means:
- copy all generated files,
- delete obsolete files in destination,
- do not touch `.git`,
- do not overwrite/remove `.nojekyll`.

This is exactly the kind of command you asked for in previous work.

### 30.2 If you want `.nojekyll` copied from source instead
Then do not exclude it and ensure it exists in the build output.

But do not accidentally delete it during sync unless you know what you are doing.

---

## 31. GitHub Remote Setup

A Git repository is local until connected to a remote.

### 31.1 View remotes
```bash
git remote -v
```

### 31.2 Set SSH remote
```bash
git remote set-url origin git@github.com:LaboratorioSperimentale/Seminari-Lab-Lilec.git
```

This changes which remote repository the local repo points to.

It does **not** mean “sync with some local folder.” It changes the remote endpoint for push and pull.

That confusion is basic but common.

---

## 32. HTTPS vs SSH for GitHub

### HTTPS
Can work, but password authentication is not supported for Git operations. You need a token.

### SSH
Usually better for a long-term workstation setup.

Once configured properly, it avoids repeated credential friction.

### Typical SSH setup
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Then add the public key to GitHub.

Test:

```bash
ssh -T git@github.com
```

This is the sane route if you do command-line Git frequently.

---

## 33. Basic Git Command Set You Actually Need

These are the commands that matter operationally.

### 33.1 Clone
```bash
git clone git@github.com:LaboratorioSperimentale/Seminari-Lab-Lilec.git
```

### 33.2 Status
```bash
git status
```

### 33.3 Add changes
```bash
git add .
```

### 33.4 Commit
```bash
git commit -m "Describe the change clearly"
```

### 33.5 Push
```bash
git push origin main
```

### 33.6 Pull
```bash
git pull origin main
```

### 33.7 Create branch
```bash
git checkout -b feature/topic-generation
```

### 33.8 Switch branch
```bash
git switch main
```

### 33.9 View branches
```bash
git branch
```

### 33.10 View history
```bash
git log --oneline --graph --decorate --all
```

If you do not know these comfortably, you are not managing the project; the project is managing you.

---

## 34. Initial GitHub Pages Setup

A standard workflow is:

1. Push `main` to GitHub.
2. Create/push `gh-pages`.
3. In repository settings, configure Pages to deploy from `gh-pages` root.
4. Ensure `.nojekyll` exists if needed.

If GitHub Actions is used instead, the settings will point to the action-based deployment mechanism.

---

## 35. GitHub Actions Deployment Strategy

For a more mature workflow, GitHub Actions can automate build and publication.

Conceptually:

- on push to `main`,
- set up Node,
- install dependencies,
- optionally set up Python,
- run Python generation,
- run Quartz build,
- deploy the built site.

This avoids manual pushing of build artifacts.

### Why this is better long-term
- reproducible,
- less human error,
- no need to commit generated site manually,
- cleaner operations.

### Why it is not always best immediately
- more moving parts,
- more debugging during initial setup,
- not ideal until local builds are already stable.

So the real advice is: **first make the local manual pipeline work flawlessly, then automate it.**

---

## 36. Example Local Build Sequence

From the project root:

```bash
source .venv/bin/activate
python python-nonpub/main.py
cd quartz-site/quartz-4
npm install
npx quartz build
```

Then publish:

```bash
rsync -av --delete --exclude='.git' --exclude='.nojekyll' \
  public/ ../../SeminariLabLiLeC-pages/
cd ../../SeminariLabLiLeC-pages
git add .
git commit -m "Update published site"
git push origin gh-pages
```

Adjust paths to your real folder layout.

---

## 37. Example Environment Setup Script

A helper shell script is useful for activating the correct toolchain.

For example, a script can:

- detect project root,
- activate Python venv,
- activate Node 22 via `nvm`,
- show versions,
- enter Quartz directory.

This is good practice because it reduces “wrong shell state” errors.

---

## 38. Obsidian Tree Management Rules

This is where many knowledge-base projects decay.

### 38.1 Keep content hierarchy meaningful
Use folders for major semantic divisions, not for every fleeting idea.

### 38.2 Distinguish authored content from generated navigation
A manually written seminar note is not the same thing as a generated topic page.

### 38.3 Keep hidden implementation folders clearly marked
The underscore prefix in `_intersezioni` is useful semantically, but remember that GitHub Pages/Jekyll behavior is why `.nojekyll` matters.

### 38.4 Do not rely on Obsidian-only behavior for public site logic
If a link works because Obsidian is forgiving, that proves nothing about Quartz.

---

## 39. File Naming and Slug Discipline

Good filenames are:
- readable,
- stable,
- slug-friendly,
- not overloaded.

Bad filenames are inconsistent mixtures of:
- uppercase/lowercase randomness,
- spaces and special characters used inconsistently,
- semantic encodings that belong in frontmatter instead.

If you want a multilingual or structured project, sloppy naming will become a tax on every later automation step.

---

## 40. Metadata Validation Checklist

Before building, validate:

- does every publishable page have a title?
- are required fields present?
- are thumbnail paths valid?
- are resource links valid?
- are language variants coherent?
- are tags controlled?
- are duplicate seminar pages intentional or accidental?
- are generated pages consistent with the source notes?

A robust Python validator should answer these before Quartz build starts.

---

## 41. Common Failure Modes

### 41.1 Wrong Node version
Quartz breaks or installs badly.

### 41.2 Running `npx quartz build` in the wrong directory
Command resolution fails.

### 41.3 Component not exported
Build fails or component is undefined.

### 41.4 Utility function not exported
Import errors.

### 41.5 Inconsistent frontmatter fields
Rendered pages become structurally uneven or broken.

### 41.6 Duplicate content paths
Generation logic creates collisions.

### 41.7 Sidebar polluted by implementation folders
Bad UX and confusing navigation.

### 41.8 Publication branch accidentally filled with source junk
Messy Pages deployment and unnecessary bloat.

### 41.9 `.nojekyll` removed
Underscore-prefixed directories or expected files can behave badly on Pages.

### 41.10 Remote misconfiguration
Push goes nowhere useful or fails.

---

## 42. Repository Renaming and Site URL Implications

If you rename the repository, remote URLs change and sometimes GitHub Pages URLs change too, depending on the repository type and Pages configuration.

Operationally, that means:

- update local remote URLs,
- confirm Pages settings,
- verify published URL after rename.

So yes, repository naming should be chosen deliberately early if possible.

---

## 43. Suggested `.gitignore` Logic

A serious `.gitignore` should typically exclude:

```gitignore
.venv/
node_modules/
.quartz-cache/
__pycache__/
*.pyc
build-nonpub/
dist-nonpub/
logs/
```

Possibly also OS/editor junk.

Be careful with `.obsidian/`: sometimes you want parts of it, sometimes not.

---

## 44. What Should Be Versioned

Version:
- source markdown,
- Python scripts,
- Quartz custom components,
- configuration files,
- build scripts,
- workflow files,
- essential assets.

Usually do not version:
- local virtual environments,
- dependency caches,
- transient build caches,
- machine-specific junk.

This is basic repository hygiene.

---

## 45. Suggested README Structure

Your internal project README should explain:

1. project purpose,
2. folder structure,
3. prerequisites,
4. Python setup,
5. Node setup,
6. Quartz build commands,
7. Python generation commands,
8. publication workflow,
9. troubleshooting notes.

If a collaborator cannot set up the project from the README, your project is under-documented.

---

## 46. Minimum Command Cheat Sheet

### Python
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python python-nonpub/main.py
```

### Node / Quartz
```bash
nvm install 22
nvm use 22
cd quartz-site/quartz-4
npm install
npx quartz build --serve
```

### Git
```bash
git status
git add .
git commit -m "message"
git push origin main
```

### Worktree
```bash
git worktree list
git worktree add -b gh-pages ../SeminariLabLiLeC-pages
```

### Publish
```bash
rsync -av --delete --exclude='.git' --exclude='.nojekyll' public/ ../SeminariLabLiLeC-pages/
cd ../SeminariLabLiLeC-pages
git add .
git commit -m "Publish updated site"
git push origin gh-pages
```

---

## 47. Recommended Mature End-State Architecture

The ideal mature setup is this:

### Authoring
- Obsidian vault with disciplined frontmatter and controlled taxonomy.

### Transformation
- Python scripts modularized into generators and validators.

### Rendering
- Quartz 4 customized with clean component architecture.

### Versioning
- Git repository with clean source history.

### Publication
- `gh-pages` branch or automated Pages deployment.

### Automation
- GitHub Action for reproducible build and deployment.

### Quality control
- pre-build validation reports,
- duplicate checks,
- metadata checks,
- stable naming and folder conventions.

This is not overengineering. This is the minimum level of seriousness for a project that should last.

---

## 48. What You Should Absolutely Avoid

Here is the blunt version.

Do not:

- mix authored notes and generated notes without discipline,
- trust manual editing for repeated structural tasks,
- let tags explode into uncontrolled vocabulary,
- customize Quartz before the base build works,
- publish directly from a dirty working folder without a reproducible path,
- treat GitHub Pages as if it were your development environment,
- keep changing file organization without updating scripts,
- rely on memory instead of written build instructions,
- ignore validation because “it seems to work.”

That is how small knowledge projects become unusable and embarrassing.

---

## 49. A Practical Day-to-Day Workflow

A realistic operating rhythm is:

1. Write or edit notes in Obsidian.
2. Maintain frontmatter correctly.
3. Run Python generation script.
4. Review generated topic/intersection pages.
5. Build Quartz locally.
6. Inspect the site in browser.
7. Commit source changes to `main`.
8. Publish to `gh-pages` manually or via action.
9. Verify public deployment.

This is the workflow that keeps content, automation, and publication aligned.

---

## 50. Final Strategic Summary

The architecture you have been building is sound **if** you keep the roles clean:

- **Obsidian** for content authoring,
- **Python** for transformation and semantic generation,
- **Quartz** for rendering and site UX,
- **Git/GitHub** for versioning and distribution,
- **GitHub Pages** for publication.

The core strategic move is this: **treat the whole system as a pipeline with explicit boundaries**.

That is what prevents the project from collapsing into folder spaghetti, broken links, ad-hoc scripts, and deployment confusion.

If you maintain that discipline, the system scales.
If you do not, every new feature will cost double and break something else.

---

## 51. Short Operational Appendix: Canonical Command Sequence

```bash
# 1. Enter project
cd /path/to/seminari-site

# 2. Activate Python environment
source .venv/bin/activate

# 3. Run Python preprocessing
python python-nonpub/main.py

# 4. Activate correct Node version
nvm use 22

# 5. Build Quartz
cd quartz-site/quartz-4
npm install
npx quartz build

# 6. Sync build output to Pages worktree
rsync -av --delete --exclude='.git' --exclude='.nojekyll' public/ ../SeminariLabLiLeC-pages/

# 7. Publish
cd ../SeminariLabLiLeC-pages
git add .
git commit -m "Publish latest Quartz site"
git push origin gh-pages
```

That sequence is the operational backbone.

---

## 52. Suggested Next Improvements

If this project is to become more robust, the highest-value next steps are:

1. modularize the Python script completely,
2. formalize the frontmatter schema,
3. write a validation script that fails fast,
4. stabilize the topic/intersection generation model,
5. finalize explorer filtering and site branding,
6. convert manual publication into GitHub Actions once local builds are clean,
7. document everything in a project README for repeatability.

That is the rational path forward.


---

## 53. Git and GitHub Pages Operational Command Cookbook

This section is the practical command appendix for the exact operational problems that tend to arise in a source-repo + `gh-pages` worktree workflow.

The point is not elegance. The point is to stop making avoidable mistakes.

### 53.1 Check where you are

### Print current directory
```bash
pwd
```

### Show whether this folder is a Git repository
```bash
git rev-parse --is-inside-work-tree
```

If this fails, you are not in a Git repository.

### Show the top-level root of the current repository
```bash
git rev-parse --show-toplevel
```

### Show the current branch
```bash
git branch --show-current
```

### Show branch + working status
```bash
git status
```

### Show all local and remote branches
```bash
git branch -a
```

---

### 53.2 Check another folder without moving into it

This is extremely useful for the `-pages` worktree.

### Check whether the pages folder is a Git repo
```bash
git -C ../SeminariLabLiLeC-pages rev-parse --is-inside-work-tree
```

### Show the root of that repo/worktree
```bash
git -C ../SeminariLabLiLeC-pages rev-parse --show-toplevel
```

### Show the current branch of the pages folder
```bash
git -C ../SeminariLabLiLeC-pages branch --show-current
```

### Show status of the pages folder
```bash
git -C ../SeminariLabLiLeC-pages status
```

If these fail with “not a git repository,” then one of the following is true:
- the folder path is wrong,
- the worktree was not created,
- you are pointing at an ordinary folder and pretending it is a worktree.

---

### 53.3 List and inspect worktrees

### Show all worktrees connected to the repository
```bash
git worktree list
```

### Add a worktree for an existing `gh-pages` branch
```bash
git worktree add ../SeminariLabLiLeC-pages gh-pages
```

### Create the `gh-pages` branch and its worktree in one shot
```bash
git worktree add -b gh-pages ../SeminariLabLiLeC-pages
```

### Remove a worktree registration
```bash
git worktree remove ../SeminariLabLiLeC-pages
```

### Clean stale worktree metadata
```bash
git worktree prune
```

---

### 53.4 Make sure the `-pages` folder is on the right branch

### Verify current branch in the publication folder
```bash
git -C ../SeminariLabLiLeC-pages branch --show-current
```

Expected result:
```text
gh-pages
```

### If needed, switch branch manually inside the publication folder
```bash
cd ../SeminariLabLiLeC-pages
git switch gh-pages
```

If the branch does not exist locally but exists remotely:
```bash
git switch -c gh-pages --track origin/gh-pages
```

If `gh-pages` does not exist at all yet, create it from the source repo root:
```bash
git switch main
git branch gh-pages
git worktree add ../SeminariLabLiLeC-pages gh-pages
```

---

### 53.5 Check remotes and upstreams

### Show remotes
```bash
git remote -v
```

### Show detailed branch tracking info
```bash
git branch -vv
```

### Set SSH remote URL
```bash
git remote set-url origin git@github.com:LaboratorioSperimentale/Seminari-Lab-Lilec.git
```

### Push local branch and set upstream
```bash
git push -u origin main
```

### Push `gh-pages` and set upstream
```bash
git push -u origin gh-pages
```

---

### 53.6 Inspect differences before publishing

### Show modified files in source repo
```bash
git status --short
```

### Show recent commit graph
```bash
git log --oneline --graph --decorate --all -n 20
```

### Compare current work with HEAD
```bash
git diff
```

### Compare staged changes
```bash
git diff --cached
```

### Compare local `gh-pages` with remote
```bash
git -C ../SeminariLabLiLeC-pages fetch origin
git -C ../SeminariLabLiLeC-pages log --oneline --decorate --graph gh-pages origin/gh-pages -n 20
```

---

### 53.7 Build and sync the site into the publication folder

Assume Quartz output is in `quartz-site/quartz-4/public/`.

### Safe sync preserving `.git` and `.nojekyll`
```bash
rsync -av --delete \
  --exclude='.git' \
  --exclude='.nojekyll' \
  quartz-site/quartz-4/public/ ../SeminariLabLiLeC-pages/
```

That is the correct pattern when:
- the destination is a Git worktree,
- you want obsolete published files removed,
- you do not want to destroy the `.git` directory,
- you want to preserve `.nojekyll`.

### If `.nojekyll` is generated in the source and should be copied too
Then use:
```bash
rsync -av --delete \
  --exclude='.git' \
  quartz-site/quartz-4/public/ ../SeminariLabLiLeC-pages/
```

But only do that if you are certain the build output contains the correct `.nojekyll` file.

---

### 53.8 Fully clean the publication folder contents except Git metadata

If you want to wipe the publication worktree contents but keep `.git` and `.nojekyll`, one safe method is rsync from an empty directory.

```bash
mkdir -p /tmp/empty-sync-dir
rsync -av --delete \
  --exclude='.git' \
  --exclude='.nojekyll' \
  /tmp/empty-sync-dir/ ../SeminariLabLiLeC-pages/
```

Then repopulate with the built site.

This is far safer than random `rm -rf *` stupidity.

---

### 53.9 Publish the updated site

```bash
cd ../SeminariLabLiLeC-pages
git status
git add .
git commit -m "Publish updated Quartz site"
git push origin gh-pages
```

### If there is nothing to commit
Git will tell you. That usually means:
- no changes were generated,
- sync failed,
- or you synced the wrong folder.

---

### 53.10 Recover from “wrong folder” errors

### Confirm where you are
```bash
pwd
git rev-parse --show-toplevel
git branch --show-current
```

### Confirm the publication folder independently
```bash
git -C ../SeminariLabLiLeC-pages rev-parse --show-toplevel
git -C ../SeminariLabLiLeC-pages branch --show-current
```

If one folder says `main` and the other says `gh-pages`, that is correct.

If both say `main`, you did not set up the worktree correctly.

If the `-pages` folder is not a repo, you are syncing into a dead ordinary directory, which is operational nonsense.

---

### 53.11 Recover from a broken `gh-pages` worktree

If the folder exists but is not functioning correctly:

```bash
git worktree list
git worktree remove ../SeminariLabLiLeC-pages
git worktree prune
git worktree add ../SeminariLabLiLeC-pages gh-pages
```

If the branch is not local yet but exists on remote:

```bash
git fetch origin
git worktree add ../SeminariLabLiLeC-pages -b gh-pages origin/gh-pages
```

---

### 53.12 Initial one-time setup example for a clean project

From the source repository root:

```bash
# verify repo
git status
git branch --show-current

# push main if needed
git push -u origin main

# create publication branch if it does not exist
git branch gh-pages

# create the worktree
git worktree add ../SeminariLabLiLeC-pages gh-pages

# verify it
git worktree list
git -C ../SeminariLabLiLeC-pages branch --show-current
```

Then populate it after the first build.

---

### 53.13 Useful GitHub-side checks

These are not shell commands, but they matter.

In the GitHub repository settings, verify:
- Pages is enabled,
- source is set to `gh-pages`,
- root folder is correct,
- the repository visibility matches your publication intent.

If GitHub Pages is misconfigured, your local Git discipline will not save you.

---

### 53.14 Minimal real-world publication sequence

This is the stripped operational sequence you will actually use again and again.

```bash
# source repo
cd /path/to/Seminari-Lab-Lilec
git branch --show-current
source .venv/bin/activate
python python-nonpub/main.py
nvm use 22
cd quartz-site/quartz-4
npx quartz build

# back to repo root if needed
cd ../..

# verify pages worktree
git -C ../SeminariLabLiLeC-pages branch --show-current

# sync build output
rsync -av --delete --exclude='.git' --exclude='.nojekyll' \
  quartz-site/quartz-4/public/ ../SeminariLabLiLeC-pages/

# publish
cd ../SeminariLabLiLeC-pages
git status
git add .
git commit -m "Publish latest site"
git push origin gh-pages
```

If you standardize this sequence, you eliminate most self-inflicted deployment errors.

