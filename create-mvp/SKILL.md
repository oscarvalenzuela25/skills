---
name: create-mvp
description: Crear, completar o retomar la especificación previa al desarrollo de un MVP mediante un flujo interactivo de Spec-Driven Development. Usar cuando el usuario quiera iniciar un proyecto desde una entrevista, crear la carpeta documental `docs/mvp`, continuar documentos pendientes, reconciliar producto y modelo de dominio, definir rutas, restricciones de diseño, stacks, arquitectura, tickets o verificar si el MVP está listo para comenzar frontend y backend.
---

# Create MVP

Construir de forma incremental la fuente de verdad de un MVP antes de programar. Preguntar, escribir cada respuesta en el proyecto, mantener un checklist reanudable y detenerse al completar la preparación; no implementar frontend, backend ni infraestructura.

## Resolver el proyecto

1. Inspeccionar el directorio actual antes de escribir.
2. Si contiene `docs/mvp/00-progress.md`, tratarlo como proyecto inicializado y ejecutar `scripts/inspect_progress.py <ruta>`.
3. Si no está inicializado, preguntar una sola vez qué desea hacer el usuario:
   - usar la carpeta actual;
   - usar otra carpeta existente;
   - crear una carpeta nueva.
4. Para una carpeta nueva, preguntar nombre y directorio padre. No adivinar la ubicación.
5. Confirmar la ruta absoluta elegida antes de crear archivos.
6. Ejecutar primero una simulación y revisar el destino:

```bash
python3 scripts/init_project.py --project-dir "/ruta/al/proyecto" --name "Nombre" --dry-run
```

7. Si el destino es correcto, ejecutar sin `--dry-run`. El script solo crea archivos ausentes y nunca reemplaza contenido.
8. Ejecutar `scripts/inspect_progress.py` después de inicializar o al retomar.

No crear una segunda carpeta si el usuario ya abrió la carpeta definitiva del proyecto. No inicializar Git, dependencias ni código salvo petición explícita separada.

## Fuente de verdad y continuidad

Aplicar esta precedencia:

1. Documentos aprobados dentro de `docs/mvp/`.
2. Decisiones versionadas dentro de `docs/architecture/decisions/`.
3. `AGENTS.md` del proyecto.
4. Referencias metodológicas de esta skill.
5. Memoria externa y conversación.

Tratar las referencias como método y plantilla, nunca como hechos del proyecto. Si una conversación contradice un documento aprobado, señalarlo y pedir confirmar la revisión del documento.

Leer siempre `docs/mvp/README.md`, `docs/mvp/00-progress.md` y los documentos dependientes de la etapa actual. No cargar todas las referencias a la vez: leer completamente solo la referencia indicada para la etapa.

## Ciclo interactivo obligatorio

Para cada etapa:

1. Verificar que sus dependencias estén aprobadas. No permitir saltar un bloqueo estructural.
2. Leer la referencia correspondiente y los documentos del proyecto requeridos.
3. Detectar contradicciones y vacíos que cambien alcance, reglas, entidades, permisos, flujos o implementación.
4. Formular pocas preguntas de alto impacto por turno. Agrupar preguntas relacionadas y permitir `por definir` o `no aplica` cuando no sean bloqueantes.
5. Incorporar las respuestas al documento inmediatamente para que otra sesión pueda retomar el trabajo.
6. Distinguir hechos confirmados, inferencias razonables y pendientes.
7. Presentar un resumen breve de lo escrito y los vacíos restantes.
8. Solicitar aprobación explícita antes de cambiar el estado a `aprobado` y marcar el checkbox en `00-progress.md`.
9. Al cambiar una decisión previa, identificar y desmarcar los documentos posteriores afectados.

Usar estos estados en cada documento: `pendiente`, `en progreso`, `bloqueado`, `en revisión`, `aprobado`, `no aplica`. Marcar `[x]` en el checklist únicamente para `aprobado` o `no aplica` confirmado.

No reemplazar silenciosamente documentos con contenido. Editar preservando información válida y explicar cualquier eliminación material.

## Flujo de documentos

Seguir este orden y dependencia:

| Paso | Documento | Dependencias | Referencia |
|---:|---|---|---|
| 1 | `01-interview.md` | Ninguna | `references/interview.md` y `references/vault-guide.md` |
| 2 | `02-prd-v1.md` | Entrevista | `references/prd-v1.md` |
| 3 | `03-domain-model-erd.md` | Entrevista, PRD V1 | `references/domain-model-erd.md` |
| 4 | `04-prd-v2.md` | PRD V1, ERD | `references/prd-v2.md` |
| 5 | `05-sitemap.md` | PRD V2, ERD | `references/sitemap.md` |
| 6 | `06-route-specs.md` | PRD V2, ERD, Sitemap | `references/route-specs.md` |
| 7 | `07-design-constraints.md` | Sitemap, Route Specs | `references/design-constraints.md` |
| 8 | `08-stack-frontend.md` | PRD V2, Route Specs, diseño | `references/stack-frontend.md` |
| 9 | `09-stack-backend.md` | PRD V2, ERD, Route Specs | `references/stack-backend.md` |
| 10 | `10-stack-devops.md` | Stacks frontend/backend | `references/stack-devops.md` |
| 11 | `11-architecture-overview.md` | Todos los anteriores | `references/architecture-overview.md` |
| 12 | `12-kanban.md` | Route Specs, stacks, arquitectura | `references/kanban.md` |
| 13 | `13-readiness-review.md` | Todos los anteriores | `references/readiness-review.md` |

Consultar `references/vault-sources.md` para la procedencia y alcance de las referencias.

## Reglas por etapa

### Entrevista

No aceptar una entrevista vacía como completada. Hacer una entrevista adaptativa y escribir respuestas parciales. Incluir rutas de autenticación, recuperación, settings, mantenimiento y 404 solo cuando el producto y su sistema de usuarios las justifiquen.

### PRD y dominio

No inventar módulos, dashboards, analytics o integraciones. En PRD V2 reconciliar explícitamente comportamiento y ERD. Usar encabezados Markdown normales en lugar de toggles de Obsidian.

### Sitemap y Route Specs

Crear solo rutas respaldadas por flujos reales. No convertir cada acción CRUD en una ruta. Cada Route Spec debe permitir implementar sin inventar qué muestra, qué hace, qué datos usa, qué reglas aplica y qué debe soportar backend.

### Diseño

Preguntar primero sistema visual, referencias, color, tipografía, accesibilidad y densidad. No asumir MUI. Generar paletas MUI y considerar el enlace de Figma de la guía solo si el usuario confirma MUI. Si el diseño se hará en una herramienta externa, documentar decisiones y enlaces; no bloquear la especificación por no poder operar esa herramienta.

### Stacks

Preguntar primero restricciones y nivel de experiencia. Recomendar una opción mínima coherente con el MVP. Preguntar únicamente categorías aplicables; no obligar al usuario a seleccionar cada herramienta del catálogo. Registrar alternativas descartadas solo cuando expliquen una decisión importante.

### Arquitectura, Kanban y preparación

Reconciliar módulos, datos, rutas, contratos, seguridad, despliegue y observabilidad antes del Kanban. Crear tickets por ruta y separar frontend/backend solo cuando corresponda. Finalizar con una revisión trazable de completitud; no declarar el MVP listo si quedan bloqueos críticos.

## Cierre

Cuando `13-readiness-review.md` esté aprobado:

- marcar el proceso como preparado para implementación;
- resumir alcance, riesgos y primer bloque de tickets;
- indicar que el trabajo futuro debe continuar desde los documentos del proyecto;
- no iniciar implementación automáticamente;
- conservar `create-mvp` como herramienta de revisión o actualización, no como requisito para cada sesión.
