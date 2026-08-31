# File & Folder Naming Convention

## Rule

Use **kebab-case** for all folder and file names. Reserve **underscore** only
for the version suffix.

```
bracket-mount_v01.sldprt
arm-joint.SLDPRT
02-leccion-croquis/
cswa-prep/
```

## Why

- **Windows/NTFS is case-insensitive, git is not.** CamelCase or PascalCase
  names can be typed consistently but still collide or get silently
  normalized across OS/tools. All-lowercase kebab-case removes that risk
  entirely.
- **Underscores collide with SolidWorks' own auto-generated names**
  (config names, design table exports). Keeping underscore reserved for
  version tags only avoids confusing your names with SolidWorks-generated
  ones.
- **No spaces, ever.** Spaces break scripts, LFS, and some URL/CLI
  operations.
- **Leading zeros on numbered folders** (`01-`, `02-`...) so they sort
  correctly in any file explorer or terminal, not just up to 9.

## Version suffix

Bump `_v01` → `_v02` only on save-worthy milestones (finished piece, major
change) — not every save. Matches the repo's commit cadence.

## Exceptions

- **Instructor Resources / Provided Files:** Instructor-provided resource folders (such as `99-resources/`) and their internal contents are **exempt** from this convention. Do not rename or alter existing instructor file names, as doing so will break internal assembly references (`.sldasm` mates and links).

## Note

This is a locally-defined convention, not an official industry standard.
No formal naming standard mandates this exact mix — the rule here is:
**pick one scheme, write it down, never deviate.**
