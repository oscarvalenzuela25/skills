# Sitemap — Referencia original

## Contenido

- Análisis de módulos, actores y flujos.
- Validación previa de rutas.
- Criterios para crear rutas.
- Tabla del Sitemap MVP.
- Rutas dudosas y validación.

---

Antes de comenzar con este prompt necesitas tener contexto de los siguientes archivos que se encuentran dentro de la carpeta proyectos/nombre del proyecto que se pregunto en un comienzo.
- Modelo de dominio ERD
- PRD V2

El documento que generaras se llamara "Sitemap" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.

Quiero que actúes como **Product Designer**, **Information Architect** y **Software Specification Analyst** para un producto digital en fase de definición funcional, bajo un enfoque de **Spec-Driven Development (SDD)**.

Tu tarea es leer el contexto y generar un **Sitemap funcional del MVP**, en formato de tabla, pensado para que luego cada ruta pueda convertirse en un **Route Spec** y servir como base directa para desarrollo.

---

## Objetivo

Definir las rutas principales del producto de forma clara, útil y aterrizada al MVP.

Este sitemap debe servir para:

- traducir módulos y flujos del sistema en rutas reales
- dejar claro qué pantallas o vistas necesita el MVP
- preparar el paso hacia Route Specs
- ayudar a implementar por ruta, considerando front, back y dependencias funcionales
- evitar rutas innecesarias o aspiracionales

No quiero un sitemap inflado ni decorativo.

Quiero un sitemap **útil para ingeniería**, donde cada ruta tenga sentido funcional real.

---

## Principio de trabajo

Debes construir el sitemap **a partir de la especificación funcional**, no desde patrones genéricos de interfaces.

Eso significa que debes basarte en:

- Modelo de dominio ERD
- PRD V2

Y desde ahí identificar:

- módulos reales
- roles reales
- flujos principales
- entidades que requieren vistas
- acciones que justifican rutas
- acciones que pueden resolverse dentro de una misma ruta sin fragmentar de más

No debes crear rutas solo porque “normalmente existen”.

No debes inflar el sitemap con vistas innecesarias.

No debes separar en múltiples rutas algo que puede resolverse en una sola vista bien definida.

---

## Forma de trabajo obligatoria

### Fase 1 — Lectura y análisis funcional

Lee toda la información entregada y detecta:

- módulos reales del sistema
- objetivo del MVP
- usuarios y roles
- flujos principales
- entidades que requieren interacción directa
- acciones importantes por ruta
- restricciones por rol
- dependencias entre vistas
- rutas base necesarias del sistema
- dudas que impacten la definición del sitemap

Tu criterio debe ser:

**“¿Qué rutas necesita realmente este producto para que el MVP funcione?”**

### Fase 2 — Validación obligatoria antes de generar el sitemap

Antes de generar el sitemap, debes evaluar si falta información o si hay contradicciones importantes entre el PRD, el ERD, el PRD V2 y el resto del contexto.

Si detectas vacíos o contradicciones que cambian de forma importante:

- los módulos
- las rutas principales
- la separación de vistas
- los roles por ruta
- el flujo de navegación
- la necesidad de rutas CRUD
- la necesidad de onboarding
- la existencia de paneles separados por rol

**no debes generar todavía el sitemap completo**.

En ese caso, debes detenerte y responder primero con:

### Vacíos o contradicciones críticas detectadas

Lista breve y priorizada.

### Preguntas necesarias antes de generar el sitemap

Haz preguntas concretas y agrupadas por tema, por ejemplo:

- módulos
- roles
- ownership
- navegación
- CRUD real por entidad
- onboarding
- auth
- separación por vistas
- paneles por rol
- acciones que requieren ruta propia

Haz solo preguntas que realmente cambien el sitemap.

No hagas preguntas cosméticas.

No hagas preguntas que puedan resolverse razonablemente desde el contexto ya entregado.

### Fase 3 — Generación del sitemap

Solo cuando la información sea suficientemente sólida, genera el sitemap completo.

Si todavía existen vacíos menores no bloqueantes:

- genera el sitemap igualmente
- marca esas rutas o decisiones como provisionales
- repórtalas en la sección de rutas dudosas o futuras

---

## Lineamientos SDD obligatorios

Quiero que el sitemap siga principios de desarrollo basado en especificaciones.

Eso implica:

- que cada ruta tenga sustento funcional claro
- que cada ruta pueda derivar luego en un Route Spec
- que cada ruta responda a un flujo, caso de uso o necesidad real
- que los roles por ruta sean coherentes con el dominio
- que la agrupación por módulo tenga sentido funcional
- que el sitemap refleje el MVP real y no una visión aspiracional
- que se diferencie claramente entre:
    - rutas confirmadas por el contexto
    - rutas inferidas razonablemente
    - rutas dudosas o futuras

Si una ruta no está suficientemente respaldada por módulos, flujos, entidades o reglas, no debe consolidarse como ruta firme del MVP.

Si una acción puede resolverse dentro de una vista existente, no debes crear una ruta adicional sin justificación clara.

---

## Qué debes hacer

- Detectar los módulos reales del sistema.
- Proponer solo rutas justificadas por el contexto.
- Evitar inflar el sitemap con vistas innecesarias.
- Asignar roles a cada ruta.
- Agrupar correctamente cada ruta dentro de un módulo.
- Si una ruta parece dudosa o futura, marcarla como tal en una sección aparte.
- Pensar este sitemap como base directa para Route Specs y desarrollo por ruta.

Las rutas base de todo sistema son:

- `login`
- `register`
- `recovery-password`
- `maintenance`
- `404`
- `onboarding` (solo si el registro no pide la información personal necesaria)
- `settings`

Pero estas rutas base **solo deben incluirse si aplican al producto y al flujo real definido**.

No las agregues mecánicamente si el contexto indica otro enfoque.

---

## Criterios para decidir si una ruta merece existir

Antes de agregar una ruta, debes validar al menos una de estas razones:

- soporta un flujo principal del MVP
- soporta una entidad con interacción propia relevante
- soporta una acción que no cabe razonablemente dentro de una vista existente
- requiere separación por rol
- requiere una vista dedicada por complejidad funcional
- requiere una experiencia distinta de creación, detalle, edición o gestión

Si no cumple una razón clara, no la agregues.

---

## Formato de salida

Crear un documento llamado "Sitemap"

**Sitemap MVP**

Dentro de esa sección, crear una **tabla** con estas columnas:

- **Ruta**
- **Roles**
- **Módulo**
- **Objetivo**
- **Prioridad**

---

## Reglas para completar la tabla

- **Ruta**: path funcional propuesto
- **Roles**: roles que usan esa ruta
- **Módulo**: módulo funcional al que pertenece
- **Objetivo**: para qué existe esa ruta, en una frase corta
- **Prioridad**: `MVP` o `Futuro`

---

## Reglas importantes

- No crear rutas aspiracionales.
- No agregar analytics, reportes, auditoría, settings avanzados, centro de ayuda o features futuras si no están respaldadas por el contexto.
- Si una acción puede resolverse dentro de una vista existente, no crear una ruta extra sin justificación.
- Mantener el resultado simple, claro y útil para pasar a Route Specs.
- Escribir pensando en desarrolladores.
- No separar vistas por costumbre si no hay una razón funcional.
- No crear CRUDs completos automáticamente si el contexto no los exige.
- No inventar dashboards o paneles si no están sostenidos por el dominio y los flujos.

---

## Entregable adicional

Debajo de la tabla, agregar una sección breve llamada:

**Rutas dudosas o futuras**

Ahí listar:

- rutas que sobran
- rutas que podrían fusionarse
- rutas que conviene dejar para después
- rutas que dependen de una definición pendiente
- rutas que fueron inferidas pero no están totalmente confirmadas

---

## Recomendación interna para construir el sitemap

Antes de proponer rutas, piensa así:

1. qué módulos existen
2. qué actor usa cada módulo
3. qué flujos clave deben ocurrir
4. qué vistas mínimas necesita cada flujo
5. qué acciones caben dentro de una misma ruta
6. qué realmente necesita una ruta propia

Esto es importante porque el objetivo no es listar páginas, sino definir una estructura de navegación mínima y funcional para el MVP.

---

## Validación obligatoria antes de entregar

Antes de entregar el sitemap, revisa internamente:

- si cada ruta tiene justificación funcional real
- si el conjunto de rutas cubre los flujos principales del MVP
- si los roles por ruta tienen sentido
- si hay rutas redundantes que podrían fusionarse
- si agregaste rutas que realmente no estaban respaldadas
- si el sitemap quedó útil para pasar a Route Specs
- si el resultado refleja el MVP real y no una expansión futura del producto

Corrige cualquier exceso antes de entregar.
