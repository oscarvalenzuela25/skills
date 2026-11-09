# Operación del backend desde la definición del MVP

Leer cuando el proyecto necesita backend propio o gestionado, funciones o trabajos en segundo plano. El objetivo es acordar cómo se verificará, desplegará y operará desde el inicio; esta skill documenta decisiones y tickets, no provisiona infraestructura ni instala instrumentación.

## Entrevista temprana

Agrupar las preguntas según lo que ya se conozca; no volver a preguntar decisiones confirmadas ni recorrer todas las opciones del catálogo. Si el usuario no tiene experiencia, explicar el resultado de cada capacidad y proponer un mínimo según riesgo/presupuesto.

- **Uso y responsabilidad:** ¿será un prototipo local, un piloto con usuarios reales o un servicio productivo? ¿Qué ocurre si falla o pierde datos, cuánto tiempo puede estar detenido y quién responderá?
- **CI/CD:** ¿quiere validaciones automáticas al subir cambios? ¿Despliegue manual, automático o promoción deliberada entre entornos? ¿Tiene repositorio, ramas y proveedor definidos? CI no implica CD automático.
- **Monitoreo y alertas:** ¿cómo sabremos si la API deja de responder, una dependencia falla o un job queda detenido? ¿Quién recibe la alerta y por qué canal? Separar revisión manual, chequeo externo y métricas según el alcance.
- **Logs:** ¿qué necesitamos diagnosticar y dónde se consultará? Acordar correlación de peticiones/trabajos, errores, acceso, retención y tratamiento de datos sensibles. Los logs no sustituyen métricas ni alertas.
- **Seguridad y datos:** ¿qué rutas son públicas, quién accede a cada recurso y qué datos/secretos se manejan? ¿Cómo se configurarán permisos, exposición de servicios, TLS y dependencias? No presentar la protección de credenciales o datos como algo que puede omitirse por ser un MVP.
- **Datos y recuperación, si aplica:** ¿qué datos deben recuperarse, con qué pérdida y demora tolerables, y cómo se comprobará un restore? Si hay jobs o integraciones, preguntar por reinicio, concurrencia y resultados inciertos, sin asumir que reintentar siempre es seguro.

No imponer GitHub Actions, una estrategia de ramas, un proveedor, una retención o herramientas como APM/tracing por defecto. Un prototipo local puede posponer servicios externos; registrar cómo se depura y qué tendrá que resolverse antes de exponerlo a usuarios. Si no hay backend, marcar este alcance como no aplicable y tratar sólo las necesidades reales del frontend/hosting.

## Registro y trazabilidad

| Documento | Qué debe registrar |
| --- | --- |
| `01-interview.md` | Uso, impacto de fallos, datos sensibles, presupuesto, operador y preferencias sobre CI/CD, monitoreo, logs y seguridad |
| `09-stack-backend.md` | Señales/contratos de salud, errores y correlación; límites de dependencias/jobs; controles de seguridad y configuración que el backend debe soportar |
| `10-stack-devops.md` | Entornos, ramas/promoción, validaciones, entrega/rollback, secretos, recopilación/retención de logs, monitoreo/alertas, responsable y backups cuando apliquen |
| `11-architecture-overview.md` | Responsabilidad del backend, plataforma/proveedor y operador; qué cambia por entorno y cómo se recupera |
| `12-kanban.md` | Tickets del mínimo acordado con dependencia, responsable y aceptación; trabajo transversal sólo si tiene necesidad real |
| `13-readiness-review.md` | Decisiones críticas resueltas y tickets operativos trazables; pendientes reversibles con fecha o condición de resolución |

En cada tema conservar: **decisión**, **estado** (definido, pendiente, pospuesto o no aplica), **motivo/impacto**, **responsable**, **cuándo resolver**, **ticket** y **evidencia esperada**. No inventar métricas, umbrales, disponibilidad, costos o garantías para completar la tabla. Las decisiones del usuario no demuestran implementación; las garantías de un plan se comprueban cuando se elige el proveedor.

Para proyectos retomados, revisar estos puntos al entrar a Backend/DevOps o readiness. Una omisión histórica no obliga a rehacer documentos aprobados sin evaluar su impacto ni autoriza a ejecutar cambios externos.

## Mínimo a acordar y criterios de aceptación

- **Calidad y entrega:** definir checks reproducibles antes de publicar, versión identificable y recuperación de la entrega. En monorepos, componentes y dependencias compartidas deciden los jobs; no reiniciar todo por cualquier cambio.
- **Salud:** diferenciar proceso vivo de capacidad de atender con sus dependencias. Elegir comprobaciones y plazos acotados; el diagnóstico no expone secretos. Un GET de ejemplo no prueba readiness.
- **Diagnóstico:** logs de eventos/errores con correlación, campos permitidos y secretos excluidos; evitar URLs completas con query sensible y labels de métricas de cardinalidad ilimitada.
- **Señales y alertas:** escoger las necesarias para detectar el fallo relevante (disponibilidad, errores, latencia, recursos, dependencia o cola) y verificar que la notificación llega a un responsable con una acción útil. Tracing y servicios externos se añaden cuando aporten valor.
- **Seguridad y recuperación:** definir límites/autorización por recurso, secretos por entorno, TLS, exposición de administración y tratamiento de errores; comprobar restore/reinicio si hay estado duradero. Los datos sintéticos sirven para ensayar fallos sin usar secretos productivos.

No bloquear el inicio de código porque falte un dashboard futuro o un proveedor reversible. Sí identificar como bloqueante una indefinición que cambie permisos, datos, contratos o recuperación crítica. La aprobación de readiness habilita implementar lo especificado; habilitar producción requiere verificar los controles del entorno que corresponda. Nunca marcar monitoreo activo sólo porque se creó su documento o ticket.

## Referencias de apoyo

- [OpenTelemetry: señales](https://opentelemetry.io/docs/concepts/signals/) para distinguir logs, métricas y trazas sin imponer su implementación.
- [OWASP: logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) para diseño, exclusión de datos y operación de registros.
