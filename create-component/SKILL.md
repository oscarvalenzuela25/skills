---
name: create-component
description: Guia operativa para crear componentes React/MUI con la estructura y convenciones del proyecto; cargarla antes de crear o modificar un componente.
---

## When to Use

Use this skill when:

- Creas un componente nuevo (carpeta propia o dentro de otro módulo).
- Añades lógica dedicada (custom hooks o servicios) a un componente existente.
- Incorporas MUI en un componente y necesitas confirmar patrones o props (consulta la doc vía MCP de MUI).

---

## Context

- Proyecto React 17.0.2 con webpack 5 y Styled Components; usa `theme.palette.primary.main` del theme para color de marca.
- Todo texto se traduce via `useTranslate`/`useTranslation` y se agrega en `src/translations/*`.
- Axios: usa `instance`, `pythonInstance` o `nineBoxInstance` desde `src/config/configAxios.js`.
- Prefiere React Query para datos; componentes base con MUI cuando aplique.

## Critical Patterns

### Pattern 1: Estructura del componente

```
XComponent/
├── XComponent.jsx       # UI (arrow function)
├── styles.js            # styled components usando theme
├── index.js             # export default XComponent
├── types.js             # tipos compartidos del folder (opcional)
├── hooks/               # lógica reusable (useXComponent, etc.)
├── infrastructure/      # HTTP + React Query (services.js, useServices.js)
```

- Nombra el componente y carpeta en PascalCase. Hooks en camelCase con prefijo `use`.
- Si no hay lógica adicional, omite carpetas vacías.

### Pattern 2: Firma y traducciones

```jsx
import { useTranslation } from "react-i18next";

const XComponent = (
  {
    /* props */
  }
) => {
  const { t } = useTranslation("namespace"); // aliaséalo como useTranslate si existe wrapper local
  return <Wrapper>{t("namespace.key")}</Wrapper>;
};
```

- Usa arrow function.
- Todo copy va en traducciones; crea/actualiza el JSON correspondiente y usa el hook de traducción del proyecto (`useTranslate`/`useTranslation`).
- Si usas MUI, consulta props/comportamiento con el MCP de MUI (elige la versión según `package.json`).

### Pattern 3: Estilos y datos

```jsx
// styles.js
export const Wrapper = styled.div(({ theme }) => ({
  display: "flex",
  color: theme.palette.primary.main,
}));
```

- Siempre Styled Components con theme (colores desde `palette`, no primario default de MUI).
- Para datos/HTTP:
  - `infrastructure/services.js`: handlers con el axios instance correcto.
  - `infrastructure/useServices.js`: React Query (`useQuery`/`useMutation`) usando esos handlers; favorece optimistic updates.
  - Custom hooks en `hooks/` para separar lógica de la UI.

### Pattern 4: Nomenclatura en `services.js`

- `GET` (fetch): el handler debe comenzar con `get`.
  - Ejemplo: `getNotificationTemplateDetails`.
- `PUT`: el handler debe comenzar con `update`.
  - Ejemplo: `updateNotificationTemplateSubject`.
- `POST`: el handler puede comenzar directamente con el nombre de la acción (sin prefijo obligatorio).
  - Ejemplo: `sendNotificationTemplateTestEmail`, `rollbackHeaderContent`.
- `PATCH`: misma regla que `POST` (sin prefijo obligatorio).
  - Ejemplo: `toggleNotificationStatus`.
- `DELETE`: el handler debe comenzar con `delete`.
  - Ejemplo: `deleteNotificationTemplate`.

### Pattern 5: Guardrails Anti-Warnings (React)

- Keys de listas:
  - Nunca uses objetos como `key` (`key={item}` cuando `item` es objeto termina en `[object Object]`).
  - Usa una key primitiva y estable (`id`, `slug`, `employee_id`, etc.).
  - Evita `index` como `key` salvo casos controlados de skeletons estáticos.
- PropTypes:
  - En `oneOfType`, usa solo validadores de PropTypes.
  - Para `null`, usa `PropTypes.oneOf([null])` (no `PropTypes.null`).
  - Usa `PropTypes.bool` (no `PropTypes.boolean`).
  - No uses expresiones como `PropTypes.object || PropTypes.string`; usa `PropTypes.oneOfType([...])`.
- Props custom al DOM:
  - No propagues props internas a elementos DOM/MUI base (`active`, `mobile`, `isMinimized`, etc.).
  - En styled-components usa props transientes (`$active`, `$sub`) o filtra props antes de renderizar.
- Requeridos vs opcionales:
  - Si un prop puede llegar `undefined` en runtime, no lo marques `.isRequired`.
  - Define `defaultProps`/fallbacks consistentes para evitar warnings de props faltantes.

### Pattern 6: Guardrails Anti-Warnings (Storybook y `packages/ui/src`)

- Evita JSX en constantes top-level con imports de MUI íconos/componentes.
  - No: `const iconMap = { Star: <StarIcon /> }`
  - Sí: `const iconMap = { Star: StarIcon }` y renderiza dentro del componente (`<IconComponent />`).
- Interop de imports MUI en paquete UI:
  - Cuando el componente del paquete UI se consume en app CRA/Webpack, algunos imports pueden llegar envueltos en `default`.
  - Usa un helper de unwrap (ej. `resolveModuleDefault`) para `@mui/material/*` y `@mui/icons-material/*` en componentes críticos.
- En stories:
  - Verifica que `args` no envíen objetos no renderizables como children/íconos.
  - Usa datos serializables en controles y transforma a JSX dentro del render de la story.
- Al cerrar cambios de UI package, valida:
  - `yarn workspace @nala/ui typecheck`
  - `yarn workspace @nala/ui build`
  - Confirmar que Storybook/app no muestren warnings en consola de render/prop-types.

---

## Decision Tree

```
¿Solo UI? → Crea carpeta XComponent con XComponent.jsx + styles.js + index.js.
¿Lógica reusable? → Crea hooks/useXComponent.js (y más hooks específicos si se necesitan).
¿HTTP o datos remotos? → infrastructure/services.js + infrastructure/useServices.js con React Query y axios instances.
¿Usas MUI? → Apóyate en MCP MUI para props/slots y ajusta estilos con Styled Components + theme.
¿Texto nuevo? → Añade clave en `src/translations` y úsala con `useTranslate`/`useTranslation`.
```

---

## Code Examples

### Example 1: Componente básico

```jsx
// XComponent/XComponent.jsx
import { useTranslation } from "react-i18next";
import { Wrapper, Title } from "./styles";

const XComponent = ({ titleKey }) => {
  const { t } = useTranslation("namespace");
  return (
    <Wrapper>
      <Title>{t(titleKey)}</Title>
    </Wrapper>
  );
};

export default XComponent;
```

```jsx
// XComponent/styles.jsx
import styled from "styled-components";

export const Wrapper = styled.section(({ theme }) => ({
  display: "flex",
  gap: "12px",
  color: theme.palette.primary.main,
}));

export const Title = styled.h3(() => ({
  fontSize: "18px",
  fontWeight: "bold",
}));
```

### Example 2: React Query + servicios

```jsx
// XComponent/infrastructure/services.jsx
// axiosInstance es por defecto al backend de ruby
// pythonInstance es para servicios de python
// nineBoxInstance es para servicios de ninebox (si aplica)
import axiosInstance from "src/config/configAxios";

export const getItems = (id) => axiosInstance.get(`/items/${id}`);
export const createItem = (payload) => axiosInstance.post("/items", payload);
```

```jsx
// XComponent/infrastructure/useServices.jsx
// Los mensajes casi siempre van con ese formato, pero en su totalidad siempre van en un objeto httpRequest dentro de las traducciones, con una clave específica para cada acción (ej: handleCreateItemSuccess o handleCreateItemError).
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { BASE_QUERY_OPTS } from "hooks/utils/reactQuery";
import { getItems, createItem } from "./services";
import { toast, MESSAGE_TYPES } from "components/Toast/functions";
import { handleQueryError } from "src/common/handleGenericError";
import { useTranslation } from "react-i18next";

export const useItems = ({ id, enabled }) =>
  useQuery({
    queryKey: ["items", id],
    queryFn: () => getItems(id),
    ...BASE_QUERY_OPTS,
    enabled,
  });

export const useCreateItem = () => {
  const client = useQueryClient();
  const { t } = useTranslation();

  return useMutation({
    mutationFn: ({ payload }) => createItem(payload),
    onSuccess: (data, { callback }) => {
      client.invalidateQueries({ queryKey: ["items"] });
      toast(MESSAGE_TYPES.success, {
        title: t("common:common.api_responses.success.title"),
        message: t("common:items.httpRequest.handleCreateItemSuccess"),
      });
      if (callback) callback(data);
    },
    onError: (error) =>
      handleQueryError({
        error,
        errorMessage: t("common:items.httpRequest.handleCreateItemError"),
        t,
      }),
  });
};
```

---

## Commands

```bash
npm run lint   # linting del proyecto
npm run build  # asegura que el build de producción pasa
yarn workspace @nala/ui typecheck  # validar tipos del paquete UI
yarn workspace @nala/ui build      # regenerar dist del paquete UI
```

---

## Resources

- Plantilla: usa este SKILL.md como guía base para nuevos componentes.
