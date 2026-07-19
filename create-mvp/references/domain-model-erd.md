# Modelo de dominio ERD — Referencia original

## Contenido

- Análisis funcional previo.
- Validación de vacíos de modelado.
- Reglas funcionales y técnicas.
- Entregable DBML.
- Mapeo funcional y validación.

---

Antes de comenzar con este prompt necesitas tener contexto de los siguientes archivos que se encuentran dentro de la carpeta proyectos/nombre del proyecto que se pregunto en un comienzo.
- Entrevista
- PRD V1

El documento que generaras se llamara "Modelo de dominio ERD" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.

Quiero que actúes como **Data Modeler**, **Systems Analyst** y **Software Specification Analyst** enfocado en productos SaaS y sistemas internos, bajo un enfoque de **Spec-Driven Development (SDD)**.

Tu tarea es generar un **borrador inicial de base de datos** en formato compatible con **[dbdiagram.io](http://dbdiagram.io) (DBML)**, construido **a partir de la especificación funcional entregada**, no desde supuestos técnicos arbitrarios.

---
## Objetivo

Quiero una primera propuesta de modelo relacional que me sirva como base para seguir refinando manualmente.

Este modelo debe servir para:

- validar si las entidades y relaciones del producto están bien representadas
- detectar vacíos entre el contexto funcional y el modelo de datos
- facilitar una siguiente iteración del PRD o de las especificaciones
- servir como base para conversar arquitectura, módulos y flujos

Esto debe ser un **borrador útil para ingeniería**, no un schema final de producción.

---

## Principio de trabajo

Debes modelar la base de datos **desde la especificación**.

Eso significa que debes seguir este orden mental:

1. entender el producto y su alcance
2. detectar módulos, actores, flujos y reglas
3. identificar entidades funcionales
4. identificar relaciones y ownership
5. recién después proponer tablas, campos y claves

No debes proponer tablas solo porque “normalmente existen”.

No debes agregar infraestructura, analytics, auditoría avanzada, permisos complejos o features futuras si no están justificadas por el contexto.

---

## Instrucciones

### Fase 1 — Análisis funcional previo

Antes de modelar, analiza el contexto entregado e identifica:

- problema o necesidad principal del sistema
- alcance funcional del MVP si se puede detectar
- usuarios y roles
- módulos o áreas funcionales
- flujos principales
- reglas de negocio
- ownership entre usuarios y entidades
- estados relevantes
- entidades explícitas
- entidades implícitas razonables
- dudas que impacten el modelo

Debes pensar como alguien que responde:

**“¿Qué datos necesita este sistema para soportar los comportamientos descritos?”**

### Fase 2 — Validación antes de modelar

Antes de generar el DBML, evalúa si faltan definiciones importantes.

Si faltan definiciones críticas que cambian el modelo de datos, **no generes todavía el DBML completo**.

En ese caso, debes responder con:

### Vacíos críticos para modelado

Lista breve y priorizada.

### Preguntas necesarias antes de modelar

Agrupa preguntas por tema, por ejemplo:

- entidades
- relaciones
- ownership
- estados
- roles y permisos
- cardinalidades
- autenticación
- reglas de negocio
- historial
- restricciones funcionales

Haz solo preguntas que realmente cambien el modelo.

Si la información es suficiente para avanzar, entonces sí genera el borrador DBML.

### Fase 3 — Generación del modelo preliminar

Si existen vacíos menores no bloqueantes:

- genera el DBML igualmente
- deja explícitos los supuestos
- reporta qué partes del modelo podrían cambiar en una siguiente iteración

---

## Reglas de modelado funcional

- Analiza el contexto funcional entregado.
- Identifica las entidades principales del sistema.
- Propón tablas, campos, relaciones y claves.
- Usa nombres claros y consistentes.
- Incluye `id` como clave primaria cuando tenga sentido.
- Agrega foreign keys cuando corresponda.
- Propón tipos de datos razonables.
- Crea el campo `is_active` en cada entidad padre o en una entidad que no tenga hijos, para indicar si la entidad sigue activa y evitar borrado físico cuando aplique.
- Incluye campos de auditoría básicos cuando tenga sentido, por ejemplo:
    - `created_at`
    - `updated_at`
- Agrega restricciones e índices solo cuando sean razonables.
- No inventes módulos o entidades que no estén justificadas por el contexto.
- Si hay dudas o vacíos, no los escondas: repórtalos aparte.
- Prefiere un modelo simple y funcional antes que uno sobrediseñado.
- Verifica si se utilizará un servicio de autenticación externo:
    - si sí, crea una tabla `profile` y relaciónala con la entidad del proveedor de autenticación según corresponda
    - si no, crea una tabla `users`
- Si hay relación muchos a muchos, crea tabla pivote.
- Si hay estados relevantes para el comportamiento del sistema, propón campos tipo `status`.
- Si hay ownership entre usuarios y entidades, refléjalo claramente.

---

## Lineamientos SDD obligatorios

Quiero que el modelo siga principios de desarrollo basado en especificaciones.

Eso implica:

- modelar desde comportamiento, reglas y flujos
- no modelar desde costumbre técnica
- que cada tabla tenga justificación funcional
- que cada relación soporte un flujo, regla o necesidad real
- que el modelo sea trazable al contexto entregado
- que se diferencie claramente entre:
    - información explícita del contexto
    - inferencias razonables
    - supuestos no confirmados
- que el resultado sea útil para una siguiente iteración de especificaciones

Si una regla del producto no logra reflejarse bien en el modelo, debes señalarlo.

Si existen varias formas válidas de modelar algo, elige la más simple para el MVP y aclara que es una decisión provisional.

---

## Qué debes entregar

### 1. Resumen breve

Una lista corta con:

- entidades principales detectadas
- relaciones clave
- supuestos importantes

Además, agrega un pequeño bloque llamado:

### Mapeo funcional → entidades

Relaciona de forma breve:

- módulos detectados → entidades propuestas
- flujos relevantes → relaciones necesarias
- reglas de negocio → campos o estructuras que las soportan

Esto es importante para mantener coherencia con SDD.

---

### 2. Modelo en DBML

Entrégalo en formato **[dbdiagram.io](http://dbdiagram.io) / DBML**, listo para copiar y pegar.

Debe ser un modelo preliminar, claro y consistente, útil para seguir refinando manualmente.

---

### 3. Dudas o vacíos detectados

Lista breve de cosas que faltaría definir, por ejemplo:

- estados no claros
- relaciones ambiguas
- tablas que podrían separarse más adelante
- campos que dependen de decisiones de negocio
- reglas que aún no quedan bien soportadas en el modelo
- supuestos que deberían validarse antes de pasar a implementación

---

## Reglas de modelado técnico

- Usa nombres en `snake_case`
- Usa tablas en singular o plural de forma consistente
- No metas JSON o campos genéricos tipo `data` salvo que sea realmente necesario
- No agregues tablas de configuración avanzada, permisos complejos, auditoría extensa o features futuras si no aparecen en el contexto
- No agregues tablas por costumbre si no soportan un flujo real
- No conviertas este entregable en una versión final de producción
- Prioriza simplicidad, claridad y trazabilidad funcional

---

## Formato esperado del DBML

Usa sintaxis válida de DBML, por ejemplo:

- `Table users { ... }`
- `Ref: orders.user_id > users.id`

---

## Importante

Esto debe ser un **borrador inicial útil**, no una versión final perfecta.

Quiero que priorices:

- claridad
- consistencia
- utilidad para seguir refinando en [dbdiagram.io](http://dbdiagram.io)
- alineación con la especificación funcional
- utilidad para ingeniería y siguientes iteraciones del sistema

---

## Validación obligatoria antes de entregar

Antes de entregar el resultado, revisa internamente:

- si cada tabla tiene justificación funcional
- si los flujos principales pueden sostenerse con este modelo
- si las reglas de negocio importantes tienen representación razonable
- si agregaste complejidad innecesaria
- si existe alguna entidad sugerida por el contexto que el modelo no esté reflejando
- si los supuestos importantes quedaron explícitos
- si el modelo sirve como borrador para iterar y no como diseño final sobredimensionado

Corrige cualquier exceso antes de entregar.
