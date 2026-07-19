# PRD V2 — Referencia original

## Contenido

- Comparación entre PRD V1 y ERD.
- Validación de contradicciones.
- Estructura funcional refinada.
- Ajustes, vacíos y recomendaciones.
- Validación para Sitemap y specs.

---

Antes de comenzar con este prompt necesitas tener contexto de los siguientes archivos que se encuentran dentro de la carpeta proyectos/nombre del proyecto que se pregunto en un comienzo.
- PRD V1
- Modelo de dominio ERD

El documento que generaras se llamara "PRD V2" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.

Quiero que actúes como **Product Architect**, **Systems Analyst** y **Software Specification Analyst** orientado a productos digitales que serán implementados por desarrolladores, bajo un enfoque de **Spec-Driven Development (SDD)**.


Tu tarea es leer el contexto pedido recientemente y generar un **PRD V2 más aterrizado, consistente y útil para ingeniería**, usando como base principal:

1. PRD V1
2. Modelo de dominio ERD

---

## Objetivo

Actualizar el PRD inicial para que quede mejor alineado con la realidad del sistema después de haber ajustado el modelo relacional.

Este PRD V2 debe servir como una **iteración de reconciliación entre especificación funcional y modelo de dominio**, para:

- corregir discrepancias entre PRD y BD
- aterrizar mejor entidades, módulos, flujos y reglas
- dejar más claro qué sí forma parte del MVP
- detectar pendientes reales antes de pasar a sitemap y specs
- servir como base más sólida para desarrollo

No quiero un documento ejecutivo ni inflado.

Quiero un documento corto, claro y útil para desarrolladores.

---

## Principio de trabajo

Debes construir el PRD V2 **a partir de la comparación crítica entre lo funcional y lo modelado**.

Eso significa:

1. leer el PRD V1
2. leer el modelo relacional ajustado
3. comparar ambos
4. detectar:
    - discrepancias
    - vacíos
    - reglas no soportadas
    - entidades no reflejadas
    - elementos modelados sin sustento funcional claro
5. generar una versión más consistente del PRD

No debes reescribir el PRD V1 sin análisis.

No debes asumir que el PRD V1 estaba completamente correcto.

No debes asumir que la BD ajustada está perfecta.

Debes tratarlos como insumos que deben reconciliarse.

---

## Forma de trabajo obligatoria

### Fase 1 — Lectura y comparación

Lee el PRD V1, el modelo relacional ajustado y el contexto adicional.

Compara especialmente:

- objetivo del MVP
- usuarios y roles
- módulos
- entidades
- relaciones funcionales
- reglas de negocio
- flujos principales
- ownership
- estados
- restricciones operativas

Debes identificar si existe diferencia entre:

- lo que el producto dice que debe pasar
- y lo que el modelo realmente permite representar

### Fase 2 — Validación obligatoria antes de redactar

Antes de generar el PRD V2, debes evaluar si falta información o si existen contradicciones relevantes entre el PRD V1, el modelo relacional y el contexto adicional.

Si detectas vacíos o contradicciones que cambian de forma importante:

- el alcance del MVP
- las entidades principales
- las relaciones clave
- los roles y permisos
- los estados
- las reglas de negocio
- los flujos centrales

**no debes generar todavía el PRD V2 completo**.

En ese caso, debes detenerte y responder primero con:

### Vacíos o contradicciones críticas detectadas

Lista breve y priorizada.

### Preguntas necesarias antes de generar el PRD V2

Haz preguntas concretas y agrupadas por tema, por ejemplo:

- alcance
- entidades
- relaciones
- roles
- permisos
- estados
- reglas de negocio
- ownership
- restricciones funcionales

Haz solo preguntas que realmente cambien el contenido del PRD V2.

No hagas preguntas cosméticas.

No hagas preguntas de detalle menor si el PRD puede avanzar sin eso.

### Fase 3 — Generación del PRD V2

Solo cuando la información sea suficientemente sólida, genera el PRD V2 completo.

Si todavía existen vacíos menores no bloqueantes:

- genera el PRD V2 igualmente
- marca esos puntos como pendientes
- indica qué partes podrían afectar la siguiente etapa

---

## Lineamientos SDD obligatorios

Quiero que el PRD V2 siga principios de desarrollo basado en especificaciones.

Eso implica:

- que el documento quede alineado con el comportamiento esperado del sistema
- que cada módulo tenga sustento funcional y de datos
- que cada flujo pueda traducirse después en rutas, pantallas o casos de uso
- que las reglas de negocio queden redactadas de forma verificable
- que las entidades principales estén alineadas con el modelo relacional
- que los vacíos importantes queden visibles y no escondidos
- que se diferencie claramente entre:
    - información explícita
    - ajuste inferido razonablemente
    - pendiente no resuelto

Si el modelo relacional fuerza un cambio en el PRD, debes reflejarlo.

Si el PRD propone algo que el modelo aún no soporta, debes señalarlo.

Si existe algo modelado que no tiene sustento funcional claro, debes reportarlo.

---

## Lo que debes hacer

- Leer el PRD V1 y el bloque de la BD ajustada.
- Comparar ambos críticamente.
- Detectar discrepancias entre lo funcional y lo modelado.
- Pedir aclaraciones antes de redactar si faltan definiciones importantes.
- Aterrizar mejor entidades, módulos y reglas.
- No inventar funcionalidades no respaldadas.
- Si faltan cosas importantes, no asumirlas: menciónalas como pendientes.
- Mantener el documento liviano, útil y fácil de revisar.
- Redactar pensando en ingeniería, no en stakeholders ejecutivos.
- Preparar el documento para que el siguiente paso natural sea sitemap + specs.

---

## Estructura esperada

Crear estos toggles:

- Resumen del producto
- Objetivo del MVP
- Usuarios y roles
- Alcance funcional actualizado
- Entidades principales del sistema
- Reglas de negocio actualizadas
- Flujos funcionales principales
- Ajustes detectados entre PRD y modelo
- Vacíos o dudas pendientes
- Recomendaciones para el sitemap

---

## Contenido esperado por toggle

### Resumen del producto

Versión refinada y breve del producto, ya corregida según PRD V1 + modelo relacional.

Debe explicar:

- qué es el producto
- para quién existe
- qué problema resuelve
- con foco en el MVP real

### Objetivo del MVP

Qué resuelve esta versión, ya aterrizada con la BD y el dominio modelado.

Debe dejar claro:

- qué sí cubre esta iteración
- qué resultado práctico se espera
- qué límite tiene este MVP

### Usuarios y roles

Lista clara de roles y su función principal.

Para cada rol, incluye:

- propósito dentro del sistema
- acciones principales
- relación con las entidades o módulos si aplica

### Alcance funcional actualizado

Módulos o capacidades que realmente quedan sostenidos por el PRD y la BD.

Para cada módulo, incluye:

- propósito
- acciones clave
- qué entidades lo soportan si aplica

Solo incluye lo que tenga sustento funcional razonable.

### Entidades principales del sistema

Lista de entidades principales ya alineadas con el modelo relacional.

Para cada entidad, incluye:

- qué representa
- por qué existe en el sistema
- relación funcional con otras entidades si aplica

No describas detalles técnicos de tablas o columnas.

Esto sigue siendo PRD, no documentación de base de datos.

### Reglas de negocio actualizadas

Reglas detectadas desde el PRD y la BD.

Redáctalas como reglas claras, concretas y verificables.

Incluye solo reglas funcionales importantes para el sistema.

### Flujos funcionales principales

Lista corta de acciones centrales del sistema.

Usa formato breve tipo:

- actor
- acción
- resultado esperado

Estos flujos deben ser coherentes tanto con el PRD como con el modelo relacional ajustado.

### Ajustes detectados entre PRD y modelo

Separar en:

### Lo que el PRD decía y la BD no soportaba bien

Casos donde el PRD implicaba algo que no estaba bien representado en el modelo.

### Lo que la BD tiene y el PRD no reflejaba

Casos donde el modelo incluyó entidades, relaciones o estructuras que el PRD no había dejado claras.

### Lo que fue corregido o aterrizado en esta versión

Cambios concretos que esta iteración introduce para alinear mejor producto y modelo.

Esta sección es clave y debe ser clara, breve y útil.

### Vacíos o dudas pendientes

Lista concreta de cosas que faltaría definir.

Incluye, por ejemplo:

- estados no resueltos
- relaciones ambiguas
- ownership poco claro
- reglas incompletas
- decisiones que afectan sitemap o specs
- puntos que deberían revisarse antes de implementación

### Recomendaciones para el sitemap

Observaciones breves para generar rutas reales del MVP.

Enfócate en:

- módulos que claramente deberían convertirse en rutas o secciones
- vistas mínimas necesarias
- agrupaciones razonables por rol o flujo
- dependencias entre módulos
- zonas donde el sitemap dependerá de una definición pendiente

No diseñes el sitemap completo aquí.

Solo deja insumos útiles para ese siguiente paso.

---

## Reglas importantes

- No hacer un documento largo.
- No redactar como PM ejecutivo.
- No meter teoría innecesaria.
- No inventar funcionalidades no respaldadas.
- Escribir pensando en desarrolladores.
- El resultado debe ser útil para pasar al sitemap.
- No adornar con lenguaje corporativo.
- No esconder contradicciones o vacíos.
- Si algo sigue sin resolverse, debe quedar explícito.

---

## Validación obligatoria antes de entregar

Antes de entregar el PRD V2, revisa internamente:

- si el alcance funcional realmente está sostenido por el modelo
- si las entidades principales tienen coherencia con el dominio
- si los flujos pueden sostenerse con lo modelado
- si las reglas de negocio están claras
- si eliminaste ambigüedad innecesaria del PRD V1
- si reportaste discrepancias importantes
- si el documento quedó preparado para sitemap y specs

Corrige cualquier exceso o inconsistencia antes de entregar.
