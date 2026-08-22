# Plantillas para AGENTS.md

Usar estas plantillas como contenido semántico, no como texto rígido. Adaptar nombres, comandos y secciones a la tecnología real. Preservar instrucciones existentes y evitar duplicados.

## Sección de calidad en el AGENTS.md raíz

Añadir o actualizar una única sección similar a esta:

```markdown
## Calidad del frontend

### Documentación por componente

- Cada componente nuevo debe incluir un `AGENTS.md` en la raíz de su carpeta.
- Al modificar materialmente un componente, actualiza su `AGENTS.md` en el mismo cambio.
- El archivo local documenta propósito, responsabilidades y comportamiento observable, contrato público, dependencias o efectos relevantes, cobertura y cambios materiales fechados como `YYYY-MM-DD`.
- Las reglas del `AGENTS.md` local complementan las de este archivo y se aplican al subárbol del componente.

### Pruebas unitarias e integración

- Usa el runner configurado en el proyecto.
- Coloca los tests bajo `src/tests/`, replicando la ruta de `src/`, y usa archivos `*.test.*`.
- Todo hook, handler, reducer, validator, formatter, servicio o módulo con lógica propia debe tener tests.
- Prueba comportamiento observable y estados relevantes; evita detalles de implementación y snapshots extensos.
- Toda corrección de bug debe incluir un test de regresión cuando sea viable.
- No uses APIs reales, secretos, datos de producción ni esperas arbitrarias en tests.

### Navegador y E2E

- Para exploración visual o reproducción rápida, usa primero el navegador integrado del agente cuando esté disponible.
- Para E2E automatizado y repetible, o cuando el usuario solicite un test E2E, escribe y ejecuta Playwright. Úsalo también si no existe navegador integrado.
- Prefiere selectores accesibles por role, label o texto. Usa `data-testid` solo como último recurso.
- Verifica que no aparezcan excepciones, warnings de consola ni errores de red inesperados.

### Definición de terminado

- Lint: `COMANDO_REAL`
- Typecheck: `COMANDO_REAL`
- Tests unitarios: `COMANDO_REAL`
- Coverage: `COMANDO_REAL`
- Build: `COMANDO_REAL`
- E2E: `COMANDO_REAL`
- Ejecuta los controles aplicables antes de cerrar el cambio y reporta cualquier comando no ejecutado con su motivo.
- Los cambios de UI deben revisar teclado, foco, nombres accesibles, contraste y estados responsive aplicables.
```

Reemplazar cada `COMANDO_REAL` por un script comprobado. Si una categoría no aplica, escribir `No aplica` con una razón breve; no inventar comandos.

## AGENTS.md local de un componente

Crear el archivo dentro de la carpeta del componente:

```markdown
# NombreDelComponente

## Propósito

Explica por qué existe el componente y qué necesidad de usuario o producto cubre.

## Responsabilidades y comportamiento

- Describe lo que renderiza y las interacciones que controla.
- Indica los estados relevantes: loading, empty, error, permisos, disabled o éxito, según corresponda.
- Aclara qué queda fuera de su responsabilidad cuando el límite no sea evidente.

## Contrato público

- Props, eventos, slots, children o exports relevantes.
- Supuestos e invariantes que los consumidores deben respetar.

## Dependencias y efectos

- Hooks, contextos, stores, servicios, navegación, traducciones o efectos externos relevantes.
- Requisitos de accesibilidad o responsive particulares.

## Cobertura

- Ruta de los tests unitarios o de integración en `src/tests/`.
- Escenarios cubiertos y riesgos pendientes, sin duplicar el código de los tests.

## Historial de cambios

- YYYY-MM-DD — Resumen conciso del cambio material y su motivo.
```

No convertir el historial en un log de commits. Mantener solo cambios que ayuden a un agente futuro a entender decisiones, compatibilidad o evolución del comportamiento.

## Criterios para elegir pruebas

| Cambio | Validación mínima esperada |
|---|---|
| Función pura, handler, reducer o validator | Tests unitarios de casos normales y bordes relevantes |
| Hook con estado o efectos | Tests del contrato, transiciones, errores y cleanup aplicable |
| Componente interactivo | Render, interacción por usuario, accesibilidad y estados relevantes |
| Integración con red | Mock en el límite, éxito, error y contrato de datos |
| Corrección de bug | Test que falla antes del arreglo y pasa después |
| Flujo crítico entre pantallas | Playwright E2E repetible |

La cantidad de casos depende del riesgo. No exigir tests triviales para archivos declarativos sin lógica solo para aumentar coverage.
