---
name: initial-config-frontend
description: Preparar o auditar la configuración inicial de calidad de un proyecto frontend mediante AGENTS.md raíz y por componente, pruebas unitarias o de integración y Playwright para UI y E2E. Usar al iniciar o normalizar un frontend existente; no usar para ejecutar una prueba puntual ni para proyectos sin frontend.
---

# Initial Config Frontend

Dejar un frontend existente listo para que agentes futuros documenten los componentes, prueben la lógica y puedan inspeccionar la UI de forma reproducible. Adaptarse al framework, package manager, monorepo y convenciones detectadas; preservar configuraciones válidas y cambios locales.

## Resolver el proyecto

1. Inspeccionar el directorio actual y localizar candidatos frontend mediante `package.json`, archivos fuente, scripts y dependencias del framework.
2. Si hay varios candidatos, mostrar sus rutas y pedir al usuario que elija. Si no hay ninguno, detenerse sin crear una aplicación nueva.
3. Leer todos los `AGENTS.md` aplicables, `package.json`, lockfiles y configuraciones de tests, build y TypeScript/JavaScript.
4. Revisar el estado de Git antes de editar. No sobrescribir cambios del usuario ni regenerar configuraciones completas cuando pueda hacerse una modificación localizada.
5. Detectar el package manager por el lockfile y la configuración del workspace. No mezclar npm, pnpm, Yarn o Bun ni crear un lockfile adicional.
6. Registrar una línea base: framework, lenguaje, estructura de `src`, runner unitario, Playwright, scripts ejecutables y configuración existente.

Una invocación para preparar el proyecto autoriza las instalaciones de desarrollo necesarias descritas aquí, pero no autoriza migraciones de framework, reemplazar un runner funcional, cambiar código de producto sin necesidad ni modificar CI o servicios externos fuera del repositorio.

## Configurar AGENTS.md

Leer [references/agents-templates.md](references/agents-templates.md) antes de editar instrucciones.

- Crear o actualizar el `AGENTS.md` de la raíz aplicable al frontend. Preservar sus reglas existentes y mantener una única sección de calidad frontend; actualizarla de forma idempotente en invocaciones posteriores.
- Escribir comandos reales del proyecto. No dejar placeholders ni afirmar que un comando funciona sin haberlo ejecutado.
- Incluir la obligación de crear `AGENTS.md` dentro de la carpeta de cada componente nuevo y actualizarlo cuando el componente cambie materialmente.
- El `AGENTS.md` local del componente debe documentar propósito, responsabilidades y comportamiento observable, contrato público, dependencias o efectos relevantes, cobertura y un historial conciso con fecha ISO `YYYY-MM-DD`.
- Añadir una entrada al historial solo por cambios materiales de comportamiento, contrato, dependencias o arquitectura; no registrar formato, renombres internos triviales ni cada edición de tests.
- No crear retrospectivamente un `AGENTS.md` para todos los componentes salvo que el usuario lo pida. La regla aplica a componentes nuevos y a componentes modificados durante el trabajo futuro.

## Configurar Playwright

### Detectar y conservar

1. Revisar dependencias, scripts, archivos `playwright.config.*` y carpetas E2E antes de instalar.
2. Si Playwright ya existe, conservar su organización y comprobar:
   - que la configuración carga y descubre tests;
   - que `testDir`, `baseURL` y `webServer` corresponden al proyecto;
   - que el servidor usa un script real y `reuseExistingServer` fuera de CI;
   - que retries, trace, screenshot y video producen diagnóstico útil sin ocultar fallos;
   - que no hay secretos, URLs de producción ni puertos incompatibles codificados.
3. Corregir solo los problemas comprobados. No reemplazar una configuración válida por la plantilla preferida de la skill.

### Instalar cuando falta

- Instalar `@playwright/test` como dependencia de desarrollo con el package manager detectado.
- Instalar al menos Chromium mediante el comando del propio Playwright. Si la descarga falla, no reintentar indefinidamente: conservar la configuración y reportar el comando pendiente.
- Crear `playwright.config.ts` o `.js` según el lenguaje del proyecto. Usar por defecto `e2e/` para no mezclar E2E con los tests de `src/tests`.
- Configurar `baseURL` y `webServer` solo después de identificar el comando de desarrollo o preview y su URL. Favorecer variables de entorno con un valor local seguro.
- Añadir scripts claros como `test:e2e`, `test:e2e:ui` y, si aporta valor, `test:e2e:headed`, respetando la nomenclatura existente.
- Crear un smoke test mínimo solo si existe una ruta estable que pueda verificarse sin credenciales ni datos externos.

### Política de navegador

Escribir en el `AGENTS.md` raíz:

- Usar el navegador integrado del agente, cuando esté disponible, para exploración interactiva, inspección visual y reproducción rápida de errores.
- Usar Playwright para pruebas E2E automatizadas, repetibles y versionadas, siempre que el usuario pida un test E2E, y como alternativa cuando no exista navegador integrado.
- Para selectores, priorizar roles, labels y texto accesible; usar `data-testid` solo cuando no exista un selector semántico estable.
- No considerar una inspección manual como sustituto de un test de regresión automatizado cuando cambie lógica o se corrija un bug.

## Configurar pruebas unitarias e integración

### Conservar el runner existente

1. Detectar Vitest, Jest u otro runner mediante dependencias, scripts y configuración.
2. Si existe un runner funcional, usarlo y completar únicamente lo necesario para DOM, framework, setup, mocks y coverage. No instalar Vitest en paralelo.
3. Mantener convenciones existentes cuando sean coherentes con la estructura requerida. Documentar cualquier excepción.

### Instalar Vitest cuando no hay runner

- Instalar `vitest`, `jsdom` y `@vitest/coverage-v8` como dependencias de desarrollo.
- Instalar adaptadores según el framework detectado. Para React, usar `@testing-library/react`, `@testing-library/jest-dom` y `@testing-library/user-event`; para otros frameworks, usar su Testing Library o utilidad oficial equivalente.
- Crear la configuración y el archivo de setup en el lenguaje del proyecto, reutilizando aliases y transformaciones de la herramienta de build.
- Añadir scripts no ambiguos para ejecución interactiva, ejecución única y coverage. Preservar scripts existentes y evitar cambiar el significado de `test` si rompería CI.

### Estructura y alcance

Ubicar tests unitarios y de integración en `src/tests/`, replicando la estructura relativa de `src/` y usando el sufijo `.test`:

```text
src/components/Cart/Cart.tsx
src/hooks/useCart.ts
src/services/cart.ts
src/tests/components/Cart/Cart.test.tsx
src/tests/hooks/useCart.test.ts
src/tests/services/cart.test.ts
```

- Probar todo hook, handler, reducer, validator, formatter, servicio y módulo que contenga lógica propia.
- Probar los componentes por comportamiento observable: interacción, accesibilidad y estados relevantes como loading, empty, error, permisos y éxito. Evitar acoplar tests a detalles internos.
- Cada corrección de bug debe incluir un test de regresión cuando sea técnicamente viable.
- Aislar red, reloj, aleatoriedad, storage y otras fuentes no deterministas. No llamar servicios reales ni depender de datos de producción.
- Preferir mocks en límites externos y lógica real dentro del módulo. No abusar de snapshots ni de mocks que solo repiten la implementación.
- Configurar coverage para medir código propio y excluir archivos generados, tipos y configuración. No imponer un porcentaje arbitrario a un proyecto existente; proponer umbrales a partir de la línea base o de una decisión explícita del usuario.

## Definición de terminado en AGENTS.md

Además de las reglas anteriores, registrar:

- los comandos reales de lint, typecheck, tests unitarios, coverage, build y E2E;
- qué comandos son obligatorios según el tipo de cambio;
- que un cambio de lógica requiere tests y que un fallo conocido no puede ocultarse eliminando o debilitando pruebas;
- que los cambios de UI deben verificar teclado, foco, nombres accesibles, contraste y estados responsive aplicables;
- que no deben introducirse warnings de consola, errores de red inesperados ni excepciones durante la validación;
- que los tests deben ser independientes del orden, repetibles y libres de esperas arbitrarias.

## Validar y cerrar

1. Verificar que las dependencias y el lockfile corresponden al package manager elegido.
2. Ejecutar la carga o listado del runner unitario y de Playwright para detectar errores de configuración incluso si todavía no hay una suite completa.
3. Ejecutar los comandos disponibles y proporcionales al cambio: tests unitarios, typecheck, lint y build. Ejecutar E2E solo cuando el entorno local pueda levantarse sin credenciales o servicios no disponibles.
4. Revisar que `AGENTS.md` contenga comandos comprobados y que los archivos de configuración no tengan placeholders.
5. Resumir archivos creados o modificados, dependencias agregadas, comandos ejecutados, resultados y cualquier paso pendiente. No declarar éxito para una validación que no se ejecutó.

La configuración debe ser reanudable e idempotente: una segunda ejecución audita y corrige, no duplica secciones, scripts, dependencias ni archivos.
