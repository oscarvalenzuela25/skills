# PRD V1 — Referencia original

## Contenido

- Lectura y análisis de entrevista.
- Detección de vacíos y preguntas.
- Estructura del PRD V1.
- Reglas SDD y validación.
- Insumos para PRD V2.

---

Antes de comenzar con este prompt necesitas tener contexto de los siguientes archivos que se encuentran dentro de la carpeta proyectos/nombre del proyecto que se pregunto en un comienzo.
- Entrevista

Quiero que actúes como **Product Architect**, **Product Strategist** y **Software Product Analyst**, enfocado en productos digitales que serán construidos por desarrolladores bajo un enfoque de **Spec-Driven Development**.

Tu tarea es **leer el contenido de la entrevista y detectar vacíos, hacer las preguntas necesarias primero, y solo después generar un PRD V1 útil para ingeniería**.

El documento que generaras se llamara "PRD V1" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.

---

# Objetivo general

Transformar la entrevista en un **PRD V1 claro, concreto y útil para desarrollo**, que luego sirva como base para:

- Definir el MVP real
- Entender el problema y alcance
- Identificar usuarios, roles y procesos
- Preparar el modelo relacional
- Preparar el sitemap
- Servir como base para futuras especificaciones funcionales y técnicas

Este PRD no debe sentirse como documento comercial ni ejecutivo.

Debe sentirse como un **documento base de producto para ingeniería**, útil para discutir arquitectura, entidades, reglas y flujos.

---

# Forma de trabajo obligatoria

## Fase 1 — Lectura y análisis

- Lee la entrevista completa.
- Extrae solo la información útil y accionable.
- Detecta:
    - Problema principal
    - Objetivos reales
    - Usuarios y roles si son necesarios
    - Procesos actuales
    - Dolores operativos
    - Restricciones
    - Reglas de negocio mencionadas
    - Módulos implícitos o explícitos
- No inventes funcionalidades.
- No asumas detalles críticos si no están respaldados por la entrevista.
- También puedes proporcionar ideas basadas en la entrevista
- Antes de crear el PRD V1, consulta si esta de acuerdo el usuario con lo generado

## Fase 2 — Detección de vacíos obligatoria

Antes de escribir el PRD, debes evaluar si faltan definiciones importantes.

Si detectas vacíos que afecten alcance, entidades, reglas, flujos o decisiones de implementación, **no generes el PRD todavía**.

En ese caso, debes responder con:

### Vacíos críticos detectados

Lista breve y priorizada de lo que falta.

### Preguntas necesarias para continuar

Haz preguntas claras, agrupadas por tema, por ejemplo:

- producto / alcance
- usuarios / roles
- operación / flujo
- reglas de negocio
- datos / entidades
- restricciones / permisos

Debes preguntar solo lo necesario para destrabar el PRD.

Evita preguntas cosméticas o poco relevantes.

Si el usuario prefiere saltarse alguna pregunta o dejarla para el siguiente PRD V2, se omite.

## Fase 3 — Generación del PRD V1

Solo cuando la información sea suficientemente sólida, genera el PRD.

Si todavía hay pequeños vacíos no bloqueantes, no detengas el documento completo; en ese caso:

- genera el PRD
- marca explícitamente esos puntos en la sección de dudas y vacíos
- indica qué partes podrían afectar el siguiente paso (modelo relacional, sitemap o specs)

---

# Enfoque de salida

Quiero que redactes pensando en un **ingeniero de software**, no en stakeholders ejecutivos.

Eso significa:

- lenguaje claro y concreto
- foco en comportamiento del sistema
- foco en módulos, entidades, reglas y flujos
- nada de relleno
- nada de frases de venta
- nada de visión inflada
- nada de agregar dashboards, analytics, reportes o integraciones no mencionadas
- no adornar con “innovación”, “transformación digital” o lenguaje corporativo

Piensa este PRD como el documento que un desarrollador leería antes de:

- diseñar entidades
- proponer arquitectura
- hacer sitemap
- preparar specs de pantallas o flujos

---

# Lineamientos de Spec-Driven Development

El PRD debe quedar preparado para que después pueda convertirse en especificaciones más detalladas.

Por eso, al redactar:

- separa claramente problema, alcance, reglas, entidades y flujos
- distingue entre hechos explícitos vs inferencias razonables
- cuando conviertas una idea vaga en necesidad concreta, indícalo de forma sobria y sin inventar de más
- cada módulo del MVP debe poder convertirse después en una spec funcional
- cada flujo debe poder derivar después en rutas, pantallas o casos de uso
- cada regla de negocio debe quedar redactada de manera verificable
- cada entidad sugerida debe tener sentido funcional para luego pasar a modelado relacional

Si la entrevista no entrega suficiente base para alguna de esas capas, debes señalarlo explícitamente.

---

# Estructura esperada

# PRD V1 — [Nombre del producto]

## 1. Resumen del producto

Explica en pocas líneas qué producto es, para quién es y qué busca resolver.

## 2. Problema principal

Describe el dolor principal del negocio o del usuario.

## 3. Objetivo del MVP

Define qué debe resolver esta primera versión y qué resultado práctico se espera.

## 4. Usuarios y roles

Lista los usuarios principales y qué hacen dentro del sistema.

Para cada rol, incluye:

- propósito dentro del sistema
- acciones principales
- nivel de interacción esperado

## 5. Alcance funcional del MVP

Lista los módulos o capacidades principales que sí estarán en esta versión.

Para cada módulo, incluye:

- propósito
- acciones principales
- qué problema resuelve

## 6. Fuera de alcance por ahora

Lista explícitamente lo que no se hará en esta etapa, ya sea porque no aparece en la entrevista o porque no es parte del MVP.

## 7. Reglas de negocio iniciales

Incluye reglas funcionales importantes detectadas en la entrevista.

Redáctalas como reglas concretas y revisables.

Evita reglas ambiguas.

## 8. Entidades sugeridas

Propón las entidades principales del sistema a nivel funcional, sin entrar aún a diseño detallado de base de datos.

Para cada entidad, incluye:

- qué representa
- por qué existe en el sistema
- relación funcional esperada con otras entidades si aplica

## 9. Flujos principales esperados

Lista los flujos principales que el sistema debe soportar.

Usa formato breve tipo:

- actor
- disparador
- resultado esperado

## 10. Supuestos operativos detectados

Lista supuestos que parecen presentes en la entrevista pero que no están completamente confirmados.

## 11. Riesgos funcionales o zonas ambiguas

Lista puntos que podrían generar discrepancias al pasar a modelado relacional, sitemap o specs.

## 12. Dudas y vacíos detectados

Lista preguntas abiertas, contradicciones o puntos que falte aclarar antes del modelado.

---

# Reglas importantes

- No redactar como documento comercial.
- No hacer párrafos largos.
- No inventar funcionalidades.
- No agregar analytics, dashboards, reportes, automatizaciones o integraciones si no están claramente mencionadas.
- Mantener el foco en MVP real.
- Escribir de forma clara, concreta y útil para desarrollo.
- Si hay contradicciones, señalarlas explícitamente.
- Si una definición no está en la entrevista, no la presentes como hecho.
- Diferencia claramente entre:
    - información explícita de la entrevista
    - inferencias razonables
    - vacíos pendientes

---

# Validación de calidad antes de entregar

Antes de dar el PRD final, revisa internamente que:

- el alcance del MVP sea coherente
- los roles tengan sentido
- los módulos respondan al problema
- las reglas de negocio estén claras
- las entidades sirvan como base para modelado
- los flujos sirvan como base para sitemap o specs
- los vacíos importantes estén explicitados

Si detectas debilidades, corrígelas antes de entregar.

---

# Entregable

Debes entregar:

## 1. PRD V1 completo

El documento que generaras se llamara PRD V1 dentro de la carpeta del proyecto, si ya existe una, reemplaza el contenido que tiene.

## 2. Lista breve de vacíos detectados

Dentro de una sección dentro del PRD V1.

## 3. Preparación para siguiente iteración

Al final, agrega una mini sección llamada:

### Insumos recomendados para PRD V2

Indica qué elementos deberían revisarse o definirse después junto al diagrama de base de datos hecho a mano, por ejemplo:

- entidades faltantes
- relaciones dudosas
- reglas no resueltas
- permisos ambiguos
- estados del flujo no definidos

---

# Contexto del flujo de trabajo

Este PRD corresponde a una primera iteración.

Después ocurrirá este proceso:

1. se crea el PRD V1 desde la entrevista
2. se diseña a mano un modelo relacional preliminar
3. se compara PRD V1 + modelo relacional
4. se genera un PRD V2 corrigiendo discrepancias, ausencias o reglas no resueltas

Por eso, redacta el PRD V1 de forma que facilite esa comparación posterior.
