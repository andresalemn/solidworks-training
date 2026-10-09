# 🎯 SOLIDWORKS Practice Problem Database & Automation Hub

Bienvenido al centro de control y base de entrenamiento con la **SOLIDWORKS Official Practice Problem Database** (365 problemas prácticos divididos en 18 niveles para las certificaciones CSWA y CSWP).

Este directorio organiza la totalidad del repositorio oficial de ejercicios de Dassault Systèmes, integrando plantillas personalizadas (`00-resources/`), carpetas estandarizadas por ejercicio y una herramienta en Python (`tracker.py`) que sincroniza el avance automáticamente en [`tracker.md`](./tracker.md).

---

## 📊 Avance Global & Tracker Interactivo

El progreso detallado ejercicio por ejercicio se administra en el archivo [**`tracker.md`**](./tracker.md).

* **Fuente Oficial:** [SOLIDWORKS Education Practice Problems](https://www.solidworks.com/solution/education/practice-problems)
* **Total de Ejercicios:** 365 problemas (250 nivel CSWA + 115 nivel CSWP)
* **Ruta del Tracker:** [`tracker.md`](./tracker.md)

---

## 🏗️ Arquitectura y Estructura de Carpetas

El directorio `practice-problems/` sigue un esquema modular estandarizado:

```text
solidworks/practice-problems/
├── README.md                           # Guía ejecutiva y documentación del sistema (este archivo)
├── tracker.md                          # Matriz interactiva de progreso (365 filas)
├── tracker.py                          # Script de automatización y sync de estado
├── 00-resources/                       # Plantillas y estándares CAD (PRTDOT, slddrt, sldstd)
├── 01-basic-sketch-extrusion/          # Nivel 01 (CSWA)
│   ├── 01.01/                          # Carpeta por problema
│   │   ├── PracticeProblems_1_1_ENG.pdf# PDF oficial de especificaciones
│   │   ├── 01.01_solucion.sldprt       # Modelo 3D resuelto (Git LFS)
│   │   └── original/                   # (Opcional) Insumos / CADs base sin modificar
│   └── ...
├── ...
└── 18-cswp-exam-level/                 # Nivel 18 (CSWP)
```

### Plantillas en `00-resources/`
Para garantizar mediciones de masa y unidades idénticas a las del examen oficial:
- `MMGS-custom.PRTDOT`: Plantilla de pieza en milímetros, gramos y segundos.
- `IPS-custom.PRTDOT`: Plantilla de pieza en pulgadas, libras y segundos.
- `a4 - landscape.slddrt` / `ISO-Horizontal.sldstd`: Formatos de hoja y estándar de dibujo 2D ISO.

---

## ⚙️ Lógica del Motor de Seguimiento (`tracker.py`)

El script [`tracker.py`](./tracker.py) analiza la presencia de archivos nativos de SOLIDWORKS (`.sldprt`, `.sldasm`, `.slddrw`) en cada carpeta de problema y actualiza [`tracker.md`](./tracker.md) automáticamente.

### 🔄 Ciclo de Vida de los Estados

| Icono | Estado | Definición | Gestión |
| :---: | :--- | :--- | :--- |
| ⬜ | **Pendiente** | Ejercicio sin iniciar o sin modelos CAD resolutivos en su carpeta. | Automática (Estado base) |
| 🟨 | **En Progreso** | Modelado iniciado a medias o requiriendo ajustes previas. | **Manual** (El script nunca modifica `🟨`) |
| ✅ | **Completado** | Ejercicio resuelto con archivos CAD guardados en su carpeta. | **Automática** via `tracker.py` / Manual |
| 🔁 | **Revisión / Repetir** | Completado pero agendado para re-practicar velocidad o estrategia. | **Manual** (El script nunca modifica `🔁`) |

### 🛠️ Reglas del Automatizador
1. **Detección de CAD:** El script escanea la carpeta asociada a cada fila `NN.MM` en busca de archivos `.sldprt`, `.sldasm` o `.slddrw`.
2. **Aislamiento de Recursos (`original/`):** Archivos CAD situados dentro de subcarpetas llamadas `original/` (como ZIPs descomprimidos con partes base del instructor) **son ignorados**. Esto previene falsos positivos donde un ejercicio no resuelto se marque como completado.
3. **Respeto de Estados Manuales:** El script **solo afecta filas con estado ⬜**. Las filas marcadas manualmente como 🟨 (en progreso), ✅ (hecho) o 🔁 (repetir) permanecen intactas.
4. **Recálculo de Estadísticas:** Actualiza en tiempo real la columna *Hechos* y *% Avance* de los 18 niveles en la tabla resumen y el total con porcentaje global (`**Total: X / 365** (Y%)`).

---

## 💻 Comandos del Tracker CLI

Ejecuta los siguientes comandos desde la terminal dentro de `solidworks/practice-problems/`:

### 1. Sincronizar Progreso (Sync)
Sincroniza y actualiza `tracker.md` tras guardar nuevos modelos CAD:
```bash
python tracker.py sync
```

### 2. Modo Simulación (Dry Run)
Inspecciona qué filas cambiarían de estado sin escribir ningún archivo:
```bash
python tracker.py sync --dry-run
```

### 3. Inicializar Estructura de Carpetas (Init)
Crea automáticamente las carpetas de problemas (`NN.MM`) faltantes en el sistema de archivos:
```bash
python tracker.py init
```

---

## 🗺️ Mapa de Niveles & Ruta de Certificación

La base de datos cubre los 18 niveles oficiales estructurados por nivel de certificación:

| Nivel | Categoría / Nombre del Nivel | Examen Target | Problemas | Features & Conceptos Clave |
| :---: | :--- | :---: | :---: | :--- |
| **01** | [Basic Sketch & Extrusion](./01-basic-sketch-extrusion/) | CSWA | 20 | Extrusión base, cotas inteligentes, relaciones geométricas |
| **02** | [Sketch Tools & End Conditions](./02-sketch-tools-end-conditions/) | CSWA | 20 | Equidistancia (Offset), Ranuras (Slots), Recorte (Trim), Hasta la superficie |
| **03** | [Global Variables & Sketch Patterns](./03-global-variables-sketch-patterns/) | CSWA | 8 | Variables globales (`A`, `B`, `C`), Matrices de croquis (Linear/Circular) |
| **04** | [Extrude Cut & Fillet/Chamfer](./04-extrude-cut-fillet-chamfer/) | CSWA | 70 | Extrusión de corte, Redondeos (Fillet), Chaflanes (Chamfer) |
| **05** | [Reference Geometry](./05-reference-geometry/) | CSWA | 15 | Planos auxiliares (Plane), Ejes de referencia (Axis), Puntos de origen |
| **06** | [Revolve Boss/Cut](./06-revolve-boss-cut/) | CSWA | 20 | Operaciones de Revolución (Saliente y Corte), Líneas de centro |
| **07** | [Feature Patterning](./07-feature-patterning/) | CSWA | 48 | Matrices de operaciones (Linear, Circular, Simetría/Mirror) |
| **08** | [Sweep Boss/Cut](./08-sweep-boss-cut/) | CSWA | 14 | Saliente/Corte Barrido (Sweep), Perfil + Trayecto, Relación de Perforar |
| **09** | [Assemblies and Mates](./09-assemblies-and-mates/) | CSWA | 16 | Relaciones de posición estándar (Coincidente, Concéntrica, Paralela) |
| **10** | [CSWA Exam Level](./10-cswa-exam-level/) | **CSWA** | 19 | Exámenes integradores completos CSWA |
| **11** | [Hole Wizard](./11-hole-wizard/) | CSWP | 12 | Asistente para Taladro, roscas, refrentados y avellanados |
| **12** | [Draft](./12-draft/) | CSWP | 9 | Ángulo de salida (Draft), caras de desmoldeo y líneas de partición |
| **13** | [Shell](./13-shell/) | CSWP | 13 | Vaciado multiespesor (Shell), caras a eliminar |
| **14** | [Rib](./14-rib/) | CSWP | 9 | Nervios (Rib), pared delgada y rigidizadores |
| **15** | [Configurations, Design Tables, Suppress](./15-configurations-design-tables-suppress/) | CSWP | 16 | Configuraciones de pieza, supresión de operaciones, tablas de diseño |
| **16** | [Global Variables, Equations, Link Values](./16-global-variables-equations-link-values/) | CSWP | 7 | Ecuaciones avanzadas, vinculación de valores paramétricos |
| **17** | [Move, Rotate, Collision & Interference](./17-move-rotate-collision-interference/) | CSWP | 14 | Detección de interferencias, movimiento mecánico, colisiones |
| **18** | [CSWP Exam Level](./18-cswp-exam-level/) | **CSWP** | 35 | Exámenes integradores completos CSWP (Multibody, Mates avanzados) |

---

## 💡 Flujo de Trabajo Recomendado

1. **Selección:** Escoge el siguiente problema disponible en [`tracker.md`](./tracker.md).
2. **Modelado:** 
   - Abre el PDF de especificaciones dentro de su carpeta `NN.MM/`.
   - Utiliza la plantilla adecuada de `00-resources/` (`MMGS-custom.PRTDOT` o `IPS-custom.PRTDOT`).
   - Resuelve la pieza respetando la intención de diseño y toma nota de tu **Tiempo real** de ejecución.
3. **Guardado:** Guarda el archivo CAD en la carpeta correspondiente `NN.MM/`.
4. **Sincronización:** Ejecuta `python tracker.py sync` para actualizar el avance en `tracker.md`.
5. **Documentación Opcional:** Completa en `tracker.md` la columna `Tiempo real` y agrega comentarios o lecciones aprendidas en la columna `Notas`.
