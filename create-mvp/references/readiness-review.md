# Revisión de preparación del MVP

## Objetivo

Verificar que una persona o agente pueda comenzar la implementación sin inventar alcance, reglas, contratos o decisiones fundamentales.

## Controles bloqueantes

- Problema, actor principal y resultado del MVP están confirmados.
- Alcance y fuera de alcance no se contradicen.
- Roles, permisos y ownership centrales están definidos.
- El ERD soporta los flujos y reglas principales.
- Cada ruta MVP tiene Route Spec suficiente.
- Estados, validaciones y casos borde críticos están documentados.
- Stacks y arquitectura son compatibles.
- Seguridad y datos sensibles tienen tratamiento definido.
- Los tickets trazan su origen y tienen criterios de aceptación.
- No quedan decisiones abiertas que cambien sustancialmente el modelo, las rutas o el alcance.

## Controles no bloqueantes

- Mejoras futuras están separadas del MVP.
- Decisiones reversibles pueden quedar `por definir` con responsable o momento de resolución.
- Observabilidad, pruebas y despliegue tienen un mínimo proporcional al riesgo.

## Operación de proyectos con backend

Verificar la trazabilidad de [backend-operations.md](backend-operations.md): las preguntas de CI/CD, monitoreo, logs y seguridad se respondieron o quedaron pospuestas/no aplicables con motivo. Comprobar decisiones críticas, responsables, momento de resolución y tickets; el mero catálogo de herramientas no basta. Datos duraderos/jobs requieren tratamiento de recuperación cuando corresponda.

Separar preparación para **implementar** de aceptación para **producción**. Un proveedor/dashboard reversible puede quedar pendiente sin bloquear código; una indefinición crítica de permisos, secretos, datos o recuperación sí necesita resolverse. Registrar riesgos y diferimientos sin afirmar que pipelines, health checks o alertas ya funcionan. No añadir una aprobación de infraestructura o contratar herramientas durante esta revisión documental.

## Estructura del entregable

1. Veredicto: `listo`, `listo con pendientes no bloqueantes` o `no listo`.
2. Resumen del alcance aprobado.
3. Matriz de controles con evidencia documental.
4. Bloqueos críticos.
5. Pendientes no bloqueantes.
6. Riesgos aceptados.
7. Primer bloque recomendado de tickets.
8. Instrucción de continuidad para el siguiente agente.

No aprobar la revisión solo porque todos los archivos existan. Comprobar su contenido y coherencia. Marcar `13-readiness-review.md` y el proceso completo como aprobados únicamente después de confirmación explícita del usuario.
