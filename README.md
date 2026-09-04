# SolidWorks Training

Personal practice repository for SolidWorks coursework, certification preparation (CSWA/CSWP), and personal CAD projects.

Since native SolidWorks files (`.sldprt`, `.sldasm`, `.slddrw`) are binary formats, they are tracked using **Git LFS** (Git Large File Storage).

---

## 📝 Course Notes & Documentation

In addition to CAD models, this repository contains detailed Markdown notes for each course module. Visitors and reviewers can browse these notes to inspect key concepts, design intent strategies, speed hacks, and troubleshooting tips.

* **Documentation Hub (`00-docs/`):** Each course workspace contains a `00-docs/` directory housing global templates and reference guides (such as `cswa-sketch-checklist.md` and `cswa-note-template.md`).
* **Lesson Notes (`README.md`):** Every lesson folder includes a dedicated `README.md` containing notes, bilingual tool glossaries, tree structures, and practical insights. These render automatically when browsing the folder on GitHub.

---

## 📦 Git LFS & Working with Binary CAD Files

Because Git is designed for text diffs, binary files can quickly inflate repository size if tracked directly in core Git. Git LFS replaces binary files in your repository with light text *pointers*, storing the actual heavy payloads on a remote LFS server.

### First-Time Setup (Per Machine)

1. **Install Git LFS globally** (only needed once per machine):
   ```bash
   git lfs install
   ```
2. **Clone and fetch binaries**:
   ```bash
   git clone <repo-url>
   cd solidworks-training
   git lfs pull
   ```
   > 💡 **Note:** Standard `git clone` downloads LFS *pointer files*. Running `git lfs pull` (or standard `git checkout` after `git lfs install`) ensures the actual binary files are retrieved.

- **Useful Commands & Step-by-Step Guide:** See [docs/git-lfs-guide.md](file:///C:/Users/52477/Documents/Sandbox/solidworks-training/docs/git-lfs-guide.md) for a detailed routine commit & push workflow.
- **Check which files are tracked by LFS:**
  ```bash
  git lfs ls-files
  ```
- **Check LFS status before pushing:**
  ```bash
  git lfs status
  ```

### CAD Repository Guidelines

- **Commit Cadence:** Commit only on milestone completions (e.g., finishing a part feature set, resolving an assembly, or completing a exercise module). Avoid committing every routine save.
- **Assembly Integrity:** Never rename or move existing part files (`.sldprt`) referenced inside assemblies (`.sldasm`), as SolidWorks stores relational file paths.
- **Instructor Assets:** Keep reference files intact to maintain internal assembly references.

---

## 📁 Repository Structure

```text
solidworks-training/
├── adnisais/
│   ├── cswa-prep/
│   │   ├── 00-docs/           # Global course templates, checklists & guidelines
│   │   ├── 01-leccion-intro/  # Lesson folder with CAD files & rendered README.md notes
│   │   ├── 02-leccion-croquis/
│   │   ├── [additional lessons...]
│   │   └── 99-resources/      # Instructor-provided reference parts & assemblies (Read-Only)
│   └── cswp-prep/
└── [new-instructor]/
    └── [new-course]/
```

- **Top-level directory:** Instructor / Author (`adnisais/`)
- **Second-level directory:** Course workspace (`cswa-prep/`)
- **`00-docs/`:** Course-wide documentation, templates, and sketch checklists.
- **Numbered directories (`01-`, `02-`):** Chronological hands-on exercises containing native SolidWorks files and a `README.md` with module notes.
- **`99-resources/`:** Provided course resources, component parts, and completed reference assemblies.

---

## 📚 Courses & Status

| Instructor | Official Course Name | Folder Name | Status |
| :--- | :--- | :--- | :--- |
| Adnisais | Curso Solidworks Básico (CSWA) | `cswa-prep` | In Progress |
| Adnisais | Curso Solidworks Básico (CSWP) | `cswp-prep` | Planned |