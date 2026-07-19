# Panel Kanban — Referencia original

## Contenido

- División de trabajo por ruta.
- Tickets frontend, backend y transversales.
- Estructura obligatoria del ticket.
- Contratos, QA y Definition of Done.
- Orden y agrupación del entregable.

---

Antes de comenzar con este prompt necesitas tener contexto de los siguientes archivos que se encuentran dentro de la carpeta proyectos/nombre del proyecto que se pregunto en un comienzo.
- Sitemap
- Route Specs

El documento que generaras se llamara "Panel Kanban" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.
Quiero que actúes como **Product Delivery Architect**, **Tech Lead funcional** y **Spec Writer** enfocado en productos digitales construidos bajo un enfoque de **Spec-Driven Development (SDD)**.

Tu tarea es transformar esa información en **tickets listos para desarrollo**, pero con una regla clave:

## Regla principal de estructuración

La unidad principal de trabajo es la **ruta**.

Debes crear tickets **a base de cada ruta definida en los Route Specs**, no a base de módulos amplios ni agrupaciones genéricas.

### Regla de división por defecto

Para cada ruta, debes evaluar si corresponde crear:

- **1 ticket Frontend**
- **1 ticket Backend**

En la mayoría de los casos, una ruta debe derivar al menos en esos dos tickets si la funcionalidad requiere UI + lógica + persistencia o integración.

### Excepción

Si detectas trabajo que **no pertenece directamente a una ruta**, sí puedes crear tickets adicionales, pero deben llevar una **etiqueta especial** que indique que no nacen desde una ruta.

Etiquetas permitidas para tickets no asociados a ruta:

- `[Shared]`
- `[Infra]`
- `[Auth Core]`
- `[Data]`
- `[QA]`
- `[Refactor]`

Ejemplos:

- `[Frontend][/login] Formulario y validaciones de acceso`
- `[Backend][/login] Autenticación con credenciales`
- `[Shared] Guards y manejo global de sesión`
- `[Infra] Configuración inicial de storage para archivos`

## Objetivo

Generar tickets que:

- nazcan directamente desde una ruta o una necesidad técnica excepcional
- reduzcan ambigüedad para desarrollo
- permitan trazabilidad entre spec funcional y ejecución
- faciliten QA
- ayuden a implementar con lógica de Spec-Driven Development

## Qué debes hacer

- Leer todo el contexto entregado.
- No inventar funcionalidades fuera de los documentos base.
- No agrupar varias rutas distintas en un mismo ticket.
- Tomar cada ruta como una unidad base de análisis.
- Para cada ruta, revisar qué necesita en frontend, backend, validaciones, permisos, estados y persistencia.
- Si una ruta requiere frontend y backend, dividirlo en tickets separados.
- Si una ruta solo requiere frontend o solo backend, dejarlo explícito.
- Si detectas una necesidad transversal no ligada a una ruta, crear un ticket especial con etiqueta permitida.
- Si algo no está suficientemente definido, no asumir demasiado: dejarlo como vacío o dependencia.

## Regla principal de SDD

Cada ticket debe dejar explícito:

- de qué ruta nace
- qué comportamiento implementa
- qué reglas de negocio aplica
- qué entra
- qué sale
- qué pasa en casos borde
- cómo se valida

## Regla de salida por ruta

Para cada ruta debes analizar primero:

### 1. Ruta analizada

Indicar:

- nombre de la ruta
- path exacto
- actor principal
- objetivo funcional de la ruta

### 2. Tickets derivados de esa ruta

Generar luego los tickets necesarios para implementar esa ruta.

Normalmente:

- un ticket frontend para la experiencia de esa ruta
- un ticket backend para la lógica y persistencia de esa ruta

Si una ruta necesita más división, puedes separar en más tickets, pero siempre manteniendo la relación clara con la ruta.

Ejemplo: Ruta: `/login`

- `[Frontend][/login] Formulario de acceso, validaciones y feedback`
- `[Backend][/login] Endpoint de autenticación y generación de sesión`

Ruta: `/pro/patients/:id`

- `[Frontend][/pro/patients/:id] Vista detalle paciente`
- `[Backend][/pro/patients/:id] Consulta de detalle paciente`
- `[Backend][/pro/patients/:id] Actualización de datos del paciente` Solo si realmente se justifica separar lectura y edición.

## Estructura obligatoria de cada ticket

# [Etiqueta][Ruta o tipo] Nombre del ticket

## 1. Objetivo

Explica en 1 a 3 líneas qué se busca resolver con este ticket.

## 2. Spec origen

Indica exactamente desde qué artefactos nace este ticket.

Formato esperado:

- PRD: [sección]
- Sitemap: [módulo/ruta]
- Route Spec: [ruta exacta]
- Modelo/Entidad: [si aplica]
- Tipo de origen: [Ruta | Transversal]

## 3. Ruta asociada

Debes indicar una de estas opciones:

- Ruta: `[path exacto]` o
- No aplica ruta: `[motivo]`

## 4. Necesidad funcional

Explica qué necesidad cubre este ticket dentro de la implementación de la ruta.

## 5. Alcance

Lista concreta de lo que sí incluye este ticket.

## 6. Fuera de alcance

Lista concreta de lo que este ticket no debe resolver.

## 7. Actor(es) involucrado(s)

Indica quién usa o afecta este flujo.

## 8. Precondiciones

Qué debe existir antes de ejecutar este comportamiento.

## 9. Disparador

Qué acción inicia este flujo.

## 10. Input

Lista los datos de entrada relevantes:

- params
- query params
- body
- formulario
- contexto
- archivos
- estado previo

## 11. Proceso / comportamiento esperado

Describe paso a paso qué debe pasar funcionalmente.

## 12. Output esperado

Qué debe producir este ticket como resultado.

## 13. Reglas de negocio

Lista reglas exactas y no ambiguas.

## 14. Casos borde y estados especiales

Evaluar según aplique:

- vacío
- loading
- error
- sin permisos
- dato inexistente
- dato duplicado
- sesión expirada
- conflicto de concurrencia
- archivo inválido
- entidad inactiva

## 15. Contrato técnico mínimo

Si aplica integración frontend/backend, definir mínimo:

### Request

- método
- endpoint
- params
- body

### Response

- estructura esperada
- códigos esperados
- errores controlados

Si no aplica API, indicar:

- `No aplica contrato API en este ticket`

## 16. Persistencia y entidades afectadas

Indica qué entidades se leen, crean, editan o relacionan.

## 17. Permisos y restricciones

Define quién puede ejecutar este comportamiento y bajo qué condiciones.

## 18. Consideraciones de UI/UX

Solo si aplica frontend.

Incluir:

- componentes clave
- estados visuales mínimos
- feedback al usuario
- mensajes de validación
- confirmaciones o alertas relevantes

## 19. Dependencias

Qué otros tickets, tablas, seeds, servicios o specs deben existir antes.

## 20. Criterios de aceptación

Lista validaciones concretas y comprobables.

## 21. Validación QA

Describe cómo probar el ticket manualmente:

- caso feliz
- caso inválido
- caso borde relevante

## 22. Riesgos o vacíos detectados

Lista ambigüedades, dependencias débiles o definición faltante.

## 23. Definition of Done

El ticket se considera terminado cuando:

- funcionalidad implementada
- criterios de aceptación cumplidos
- QA manual ejecutado
- sin errores bloqueantes
- contrato respetado si aplica
- estados borde cubiertos
- spec actualizada si hubo cambios

## Reglas importantes

- No crear tickets basados en módulos amplios si la implementación real nace desde rutas.
- No mezclar varias rutas en un solo ticket.
- Cada ticket debe poder relacionarse claramente con una ruta o con una necesidad transversal explícita.
- Si una ruta tiene frontend y backend, crear tickets separados.
- No inventar comportamiento no respaldado por PRD, Sitemap o Route Specs.
- Si falta información crítica, marcar el ticket como: `Spec incompleta` e indicar exactamente qué falta.
- Si un ticket queda demasiado grande, dividirlo, pero sin perder la referencia a la misma ruta.
- Los tickets transversales deben ser la excepción, no la regla.

## Orden recomendado de trabajo

1. Leer Route Specs
2. Tomar una ruta
3. Entender actor, objetivo, inputs, acciones y reglas
4. Derivar tickets frontend/backend de esa ruta
5. Detectar dependencias transversales si existen
6. Repetir con la siguiente ruta

## Forma esperada del entregable

Agrupa la salida por ruta.

Formato sugerido:

# Ruta: /login

## Resumen de la ruta

[breve resumen]

### Ticket 1

[Frontend][/login] ...

### Ticket 2

[Backend][/login] ...

# Ruta: /pro/dashboard

## Resumen de la ruta

...

### Ticket 1

...

### Ticket 2

...

# Tickets transversales

Solo si realmente son necesarios:

- [Shared] ...
- [Infra] ...
- [QA] ...
