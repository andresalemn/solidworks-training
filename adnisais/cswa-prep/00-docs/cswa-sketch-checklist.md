# 📋 Checklist del Croquis Robusto (SolidWorks Best Practices)

Un croquis robusto es la base de un modelo estable. Revisa esta lista antes de presionar el botón de **Extruir**, **Revolucionar** o aplicar cualquier Operación 3D.

---

### 1. Lista de Verificación General (Pre-Operación 3D)

*   [ ] **¿Anclado al Origen (0,0,0)?** El primer croquis de tu pieza debe estar relacionado directamente con el origen absoluto para evitar que se desplace libremente en el espacio 3D y cause errores en los ensambles.
*   [ ] **¿Completamente Definido (Fully Defined)?** Todas las líneas y puntos del croquis deben cambiar de color azul a **color negro**. Esto asegura que no queden geometrías libres propensas a moverse por accidente.
*   [ ] **¿Relaciones antes que Cotas?** Aplica relaciones de horizontalidad, verticalidad, colinealidad, tangencia o igualdad para simplificar tu croquis antes de saturarlo con cotas numéricas conductoras.
*   [ ] **¿Contorno Cerrado?** Si vas a hacer una extrusión o revolución estándar, verifica que no haya líneas abiertas o superpuestas que fuercen una *Operación Lámina (Thin Feature)* por accidente.
*   [ ] **¿Geometría Constructiva Adecuada?** Utilicé líneas de centro/constructivas (punteadas) para definir ejes de simetría o guías de revolución.

---

### 2. Códigos de Color Rápidos en Croquis

| Color | Estado | Significado / Reacción Recomendada |
| :--- | :--- | :--- |
| 🔵 **Azul** | Subdefinido (*Under Defined*) | Faltan cotas o relaciones. Arrastra los puntos azules con el mouse para descubrir qué libertad tiene la geometría. |
| ⚫ **Negro** | Completamente Definido (*Fully Defined*) | **¡Estado Ideal!** La geometría está fija e inalterable ante arrastres accidentales. |
| 🔴 **Rojo / Amarillo** | Sobredefinido (*Over Defined*) | Hay relaciones o cotas en conflicto o duplicadas. Elimina la cota/relación sobrante. |
| 🔘 **Gris** | Cota Conducida (*Driven*) | Cota de lectura/referencia informativa. No altera el tamaño del modelo. |
