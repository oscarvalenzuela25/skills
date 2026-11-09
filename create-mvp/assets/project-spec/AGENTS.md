# Instrucciones del proyecto: {{PROJECT_NAME}}

## Fuente de verdad

- Leer primero `docs/mvp/README.md` y `docs/mvp/00-progress.md`.
- Tratar los documentos aprobados de `docs/mvp/` como fuente de verdad del producto.
- Tratar `docs/architecture/decisions/` como fuente de decisiones técnicas versionadas.
- Si una conversación, memoria o suposición contradice un documento aprobado, detenerse y señalar la contradicción.

## Continuidad

- Retomar desde el primer paso incompleto o bloqueado del checklist.
- Leer los documentos dependientes antes de proponer cambios.
- Registrar información nueva en el documento correspondiente; no dejar decisiones importantes solo en el chat.
- Diferenciar hechos confirmados, inferencias y pendientes.
- No marcar un documento como aprobado sin confirmación explícita del usuario.
- Si cambia una decisión anterior, revisar y desmarcar los documentos posteriores afectados.

## Límite previo al desarrollo

- No comenzar frontend, backend o infraestructura mientras `13-readiness-review.md` no esté aprobado, salvo instrucción explícita del usuario.
- No inventar alcance para llenar vacíos: preguntar o marcar el pendiente y su impacto.
- Mantener `AGENTS.md` como índice de reglas; ubicar el detalle del producto en `docs/mvp/`.

## Operación desde la definición

- Si el proyecto necesita backend, preguntar desde la entrevista por CI/CD, monitoreo/alertas, logs, seguridad y recuperación aplicable.
- Registrar decisiones en `docs/mvp/09-stack-backend.md` y `docs/mvp/10-stack-devops.md`, trabajo en `docs/mvp/12-kanban.md` y su trazabilidad en `docs/mvp/13-readiness-review.md`.
- Adaptar el mínimo al riesgo/presupuesto; cada diferimiento tiene motivo, responsable y momento de resolución. No elegir proveedores o una estrategia de ramas por defecto.
- Distinguir especificación, implementación y verificación en el entorno real; un documento no demuestra monitoreo activo ni autorización para desplegar.

## Decisiones técnicas

- Crear un ADR cuando una decisión sea costosa de revertir, tenga alternativas relevantes o afecte varias partes del sistema.
- Usar `docs/architecture/decisions/ADR-template.md` como base.
