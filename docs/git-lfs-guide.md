# Git & Git LFS Workflow Guide for CAD

This guide outlines step-by-step procedures and best practices for saving, committing, and pushing SolidWorks projects tracked with **Git LFS**.

---

## 🎨 Conventional Commits with Emojis

To keep the repository history readable, organized, and colorful, follow the **Conventional Commits** standard paired with playful emojis!

### Commit Header Format

```text
<type>(<optional-scope>): <emoji> <description>
```

- **Header Rule:** Keep the total header line **under 50 characters**.
- **Body Rule:** Use an optional body paragraph separated by a blank line to explain the **what** and **why** (not the *how*).

---

### 🏷️ Commit Types & Playful Emoji Suggestions

Be creative and vary your emojis! Don't use the exact same emoji every single time—mix in colorful and unexpected choices to keep the commit graph vibrant and unique.

| Type | Purpose | Example Emojis | Example Header |
| :--- | :--- | :--- | :--- |
| `feat` | New CAD part, sketch, feature, or assembly | 🎨 🛠️ 🧱 ⚡ 🚀 🔩 💎 📐 | `feat(cswa-prep): 🔩 add bracket mount base` |
| `fix` | Fix broken mates, dimensions, or sketch errors | 🐛 🔧 🩹 🚨 🧱 🧯 💥 ⚡ | `fix(cswa-prep): 🩹 repair overdefined sketch` |
| `docs` | Documentation updates (READMEs, notes) | 📝 📚 📖 💡 ✍️ 🧾 📌 📑 | `docs(root): 📝 update git lfs workflow guide` |
| `refactor` | Reorganizing features/tree without changing geometry | ♻️ 🧹 🏗️ 📦 🪄 🔄 📐 🔀 | `refactor(cswa-prep): ♻️ simplify extrude tree` |
| `chore` | Git / LFS configuration, folder structure maintenance | 🔧 ⚙️ 🧹 📁 📦 🏷️ 🚚 🗑️ | `chore(git): ⚙️ update .gitattributes for LFS` |
| `style` | Cosmetic tweaks (appearances, colors, rendering) | 🎨 🌈 💄 ✨ 🌟 🖌️ 🎭 🔮 | `style(cswa-prep): ✨ apply polished steel finish` |

---

## 🚀 Routine Commit & Push Workflow

Follow these steps every time you finish an exercise, part, or assembly milestone and want to send your work to GitHub.

### Step 1: Open your terminal in the repo root
```bash
cd path/to/solidworks-training
```

### Step 2: Check repository status
Before staging, verify what files were added or modified:
```bash
git status
```
> 💡 **Tip:** SolidWorks creates temporary lock files (e.g. `~$part.sldprt`) while files are open. Make sure to **close SolidWorks** (or the open model) before committing so temporary lock files disappear.

### Step 3: Verify LFS is tracking your CAD files
Verify that your native CAD binaries (`.sldprt`, `.sldasm`, `.slddrw`) are tracked by Git LFS:
```bash
git lfs status
```
You should see your CAD files listed under **LFS objects to be committed**.

### Step 4: Stage your changes
Stage your modified/new files:
```bash
git add .
```

### Step 5: Create a milestone commit

Follow the format: `<type>(<optional-scope>): <emoji> <description>` (< 50 chars).

```bash
git commit -m "feat(cswa-prep): 🚀 add base plate extrusion" -m "Completed first sketch and extrude feature for the mounting block exercise to fulfill CSWA lesson requirements."
```

### Step 6: Push to GitHub
Push your local commit along with the LFS binary payloads:
```bash
git push origin main
```

---

## 🛠️ Step-by-Step Checklist (Quick Reference)

- [ ] **Close SolidWorks** to clear temporary `~$` lock files.
- [ ] Run `git status` to ensure no temporary or unwanted files are staged.
- [ ] Run `git lfs status` to confirm CAD files are detected by LFS.
- [ ] Run `git add .` to stage files.
- [ ] Write a commit message: `<type>(<scope>): <emoji> <description>` (< 50 chars header).
- [ ] Explain **what** and **why** in the commit body when needed.
- [ ] Run `git push origin main` to upload commits and LFS binary payloads.

---

## 🛑 Important Rules & Best Practices

1. **Commit on Milestones, Not Every Save:**
   - CAD binary files can't be diffed line-by-line. Commit when a feature, exercise, or assembly step is complete.
2. **Never Move or Rename Parts After Assembling:**
   - SolidWorks assemblies (`.sldasm`) reference part files (`.sldprt`) via relative/absolute file paths. Moving or renaming parts outside SolidWorks will break assembly mates.
3. **Keep Reference Folders Intact:**
   - Instructor-provided folders contain pre-linked assemblies. Keep them read-only to preserve assembly integrity.
4. **Handling LFS Storage Limits:**
   - Free GitHub accounts have monthly LFS bandwidth & storage quotas (1 GB storage / 1 GB monthly bandwidth). Pushing only major milestones helps manage this limit effectively.

