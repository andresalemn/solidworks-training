#!/usr/bin/env python3
"""Tracker de practice-problems (solo librería estándar).

  python tracker.py init            crea las carpetas vacías que enlaza el README
  python tracker.py sync [--dry-run] marca ✅ los problemas con archivos CAD y recalcula el resumen

Regla de sync: solo cambia filas ⬜. Pasan a ✅ si su carpeta contiene algún
.sldprt/.sldasm/.slddrw (fuera de una subcarpeta llamada `original`).
Nunca toca 🟨, ✅ ni 🔁: esos estados los manejas tú a mano.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

# Configurar encoding de stdout para consolas Windows (GBK / CP1252)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
README = ROOT / "tracker.md"
CAD = {".sldprt", ".sldasm", ".slddrw"}

LEVEL = re.compile(r"^## Nivel (\d+)")
ROW = re.compile(r"^\|\s*(⬜|🟨|✅|🔁)\s*\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)")
SUMMARY = re.compile(r"^\|\s*(\d+)\s*\|\s*(\[[^\]]+\]\(#nivel-\d+\))\s*\|\s*([^|]+)\s*\|\s*(\d+)\s*\|\s*\d+\s*\|\s*\d+%\s*\|")
TOTAL = re.compile(r"^\*\*Total: \d+ / \d+.*")


def read_lines():
    return README.read_text(encoding="utf-8").split("\n")


def has_cad_work(folder: Path) -> bool:
    if not folder.is_dir():
        return False
    for p in folder.rglob("*"):
        if p.is_file() and p.suffix.lower() in CAD and not p.name.startswith("~$"):
            rel_dirs = p.relative_to(folder).parts[:-1]
            if not any(d.lower() == "original" for d in rel_dirs):
                return True
    return False


def init():
    created = 0
    for line in read_lines():
        m = ROW.match(line)
        if m:
            d = ROOT / m[4]
            if not d.exists():
                d.mkdir(parents=True)
                created += 1
    print(f"Carpetas creadas: {created}")


def sync(dry_run: bool):
    original_lines = read_lines()
    lines = list(original_lines)
    level = None
    done, total, newly = defaultdict(int), defaultdict(int), []
    for i, line in enumerate(lines):
        m = LEVEL.match(line)
        if m:
            level = int(m[1])
            continue
        r = ROW.match(line)
        if not r or level is None:
            continue
        status = r[1]
        folder_path = r[4]
        problem_id = r[3]
        if status == "⬜" and has_cad_work(ROOT / folder_path):
            lines[i] = line[:r.start(1)] + "✅" + line[r.end(1):]
            status = "✅"
            newly.append(problem_id)
        total[level] += 1
        done[level] += status == "✅"

    tot_done = sum(done.values())
    tot_all = sum(total.values())
    tot_pct = round(100 * tot_done / tot_all) if tot_all else 0

    for i, line in enumerate(lines):
        s = SUMMARY.match(line)
        if s:
            n = int(s[1])
            pct = round(100 * done[n] / total[n]) if total[n] else 0
            lines[i] = f"| {n} | {s[2]} | {s[3]} | {total[n]} | {done[n]} | {pct}% |"
        elif TOTAL.match(line):
            lines[i] = f"**Total: {tot_done} / {tot_all}** ({tot_pct}%)"

    if newly:
        print("Marcados ✅:", ", ".join(newly))
    else:
        print("Sin cambios.")
    print(f"Total: {tot_done} / {tot_all} ({tot_pct}%)")
    if not dry_run and lines != original_lines:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "init":
        init()
    elif cmd == "sync":
        sync("--dry-run" in sys.argv)
    else:
        print(__doc__)
