#!/usr/bin/env python3
"""Organizador y distribuidor automático de ejercicios para practice-problems.

Lee tracker.md como fuente de verdad para mapear cada archivo (.pdf, .zip, etc.)
a su respectiva subcarpeta (ej. 05-reference-geometry/05.01/).

Uso:
  python organize.py                          # Escanea y procesa carpetas tipo LevelXX_*
  python organize.py Level05_ReferenceGeometry # Procesa una carpeta específica
  python organize.py --dry-run                 # Muestra qué se movería sin aplicar cambios
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

# Configurar encoding de stdout para consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent
TRACKER_MD = ROOT / "tracker.md"


def build_file_map():
    """Lee tracker.md y genera un diccionario: nombre_archivo_lower -> ruta_relativa_destino."""
    if not TRACKER_MD.exists():
        print(f"Error: No se encontró el archivo de referencia: {TRACKER_MD}")
        sys.exit(1)

    content = TRACKER_MD.read_text(encoding="utf-8")
    # Captura rutas del tipo: [4-1](04-extrude-cut-fillet-chamfer/04.01/PracticeProblems_4_1_ENG.pdf)
    pattern = re.compile(r"\[[^\]]+\]\((([0-1]\d-[^/]+)/([^/]+)/([^)]+\.[a-zA-Z0-9]+))\)")

    file_map = {}
    for match in pattern.finditer(content):
        rel_path = match.group(1)
        filename = match.group(4)
        file_map[filename.lower()] = rel_path
    return file_map


def find_source_folders():
    """Busca directorios entrantes tipo LevelXX_* o *Level* en la raíz."""
    candidates = []
    for p in ROOT.iterdir():
        if p.is_dir() and re.match(r"^Level\d+", p.name, re.IGNORECASE):
            candidates.append(p)
    return sorted(candidates, key=lambda p: p.name)


def clean_empty_directories(path: Path):
    """Elimina directorios vacíos recursivamente a partir de una ruta dada."""
    if not path.is_dir():
        return
    for sub in list(path.iterdir()):
        if sub.is_dir():
            clean_empty_directories(sub)
    if not list(path.iterdir()):
        try:
            path.rmdir()
        except OSError:
            pass


def organize_directory(source_dir: Path, file_map: dict, dry_run: bool = False):
    print(f"\n📂 Analizando carpeta: {source_dir.name}")
    # Buscar todos los archivos dentro de la carpeta (incluso subcarpetas)
    files = [p for p in source_dir.rglob("*") if p.is_file()]

    if not files:
        print("  ⚠️ No se encontraron archivos.")
        return 0

    moved_count = 0
    unmapped = []

    for src_file in files:
        target_rel = file_map.get(src_file.name.lower())
        if not target_rel:
            unmapped.append(src_file.name)
            continue

        target_path = ROOT / target_rel

        if dry_run:
            print(f"  [DRY-RUN] {src_file.name} -> {target_rel}")
        else:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src_file), str(target_path))
            print(f"  ✓ {src_file.name} -> {target_path.parent.name}/")
        moved_count += 1

    if unmapped:
        print(f"\n  ⚠️ Archivos sin correspondencia exacta en tracker.md ({len(unmapped)}):")
        for name in unmapped[:8]:
            print(f"    - {name}")
        if len(unmapped) > 8:
            print(f"    ... y {len(unmapped) - 8} más.")

    print(f"  ✨ {moved_count} de {len(files)} archivos organizados.")

    if not dry_run and moved_count > 0:
        clean_empty_directories(source_dir)
        if not source_dir.exists():
            print(f"  🗑️ Carpeta origen eliminada completamente (quedó vacía): {source_dir.name}")
        else:
            remaining = list(source_dir.rglob("*"))
            print(f"  ℹ️ Quedaron {len(remaining)} elementos no reconocidos en {source_dir.name}.")

    return moved_count


def main():
    parser = argparse.ArgumentParser(
        description="Distribuye automáticamente los archivos descargados de niveles a sus subcarpetas según tracker.md."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        help="Nombre o ruta de la carpeta con los ejercicios descomprimidos (ej: Level05_ReferenceGeometry). Opcional si la carpeta inicia con 'Level'.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula el proceso y muestra las rutas destino sin mover archivos.",
    )

    args = parser.parse_args()

    file_map = build_file_map()
    print(f"📚 Base de datos: {len(file_map)} archivos indexados desde tracker.md.")

    if args.folder:
        folder_path = Path(args.folder)
        if not folder_path.is_absolute():
            folder_path = ROOT / folder_path
        if not folder_path.exists() or not folder_path.is_dir():
            print(f"❌ Error: La carpeta '{folder_path}' no existe o no es un directorio.")
            sys.exit(1)
        sources = [folder_path]
    else:
        sources = find_source_folders()
        if not sources:
            print("ℹ️ No se detectaron carpetas con patrón 'LevelXX_*' en la raíz.")
            print("Puedes pasar la ruta explícita:")
            print("  python organize.py Level05_ReferenceGeometry")
            return

    total_moved = 0
    for src in sources:
        total_moved += organize_directory(src, file_map, dry_run=args.dry_run)

    print(f"\n🏁 Proceso finalizado. Total de archivos procesados: {total_moved}")


if __name__ == "__main__":
    main()
