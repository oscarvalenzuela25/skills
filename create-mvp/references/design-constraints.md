# Design Constraints — Referencia original

## Contenido

- Parámetros de color y tipado.
- Paletas light y dark.
- Estructura de theme MUI.
- Module augmentation.
- Accesibilidad y criterios de calidad.

---

Quiero que actúes como un experto en diseño de sistemas y theming para Material UI (MUI).

Necesito que generes una paleta completa para MUI a partir de un color base.

El documento que generaras se llamara "Design Constraints" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.
## Objetivo
Crear 2 variantes del theme:
1. light
2. dark

La salida debe estar lista para copiar y pegar en mi archivo de configuración de MUI.

## Parámetros de entrada
- Color base principal: {COLOR_BASE}
- Quiero la salida: {CON_TIPADO_O_SIN_TIPADO}
  - Valores posibles:
    - "con tipado"
    - "sin tipado"

## Requisitos generales
- Debes generar una paleta coherente, moderna y balanceada visualmente.
- La paleta debe sentirse profesional y apta para una aplicación real.
- Debes mantener buena accesibilidad y contraste en textos y superficies.
- El color base debe influir principalmente en `primary`, y derivar una armonía visual para `secondary` y `tertiary`.
- Los colores `primary`, `secondary` y `tertiary` deben incluir:
  - escala numérica de `50` a `900`
  - `light`
  - `main`
  - `dark`
  - `contrastText`
- El valor `500` de cada escala debe ser exactamente el mismo que `main`.
- Para `error`, `warning`, `success` también puedes incluir escala si lo consideras útil, pero como mínimo deben traer:
  - `light`
  - `main`
  - `dark`
  - `contrastText`
- `grey` debe incluir:
  - `50` a `900`
  - `A100`, `A200`, `A400`, `A700`
- Debes incluir también:
  - `background`
  - `text`
  - `border`
  - `common`
  - `info`
  - `contrastThreshold`
  - `tonalOffset`
  - `divider`
  - `action`

## Estructura requerida
La respuesta debe devolver exactamente una estructura pensada para MUI con 2 objetos:
- `lightPalette`
- `darkPalette`

## Importante sobre el tipado
Si el parámetro `{CON_TIPADO_O_SIN_TIPADO}` es:
- `"con tipado"`:
  - devuelve el código en TypeScript
  - incluye los tipos necesarios para usarlo en MUI
  - si agregas claves custom como `tertiary`, `border`, `background.surface`, `text.inverse`, etc., incluye también el ejemplo de module augmentation necesario para que MUI no marque error
- `"sin tipado"`:
  - devuelve solamente el objeto plano listo para pegar
  - sin interfaces, sin types, sin module augmentation

## Formato de salida
- Devuelve solo código
- No expliques nada fuera del código
- No agregues texto introductorio
- No uses comentarios innecesarios
- Mantén nombres claros y consistentes

## Referencia de estructura
Usa esta forma como guía de keys y organización:

{
  "mode": "light",
  "primary": {
    "50": "#...",
    "100": "#...",
    "200": "#...",
    "300": "#...",
    "400": "#...",
    "500": "#...",
    "600": "#...",
    "700": "#...",
    "800": "#...",
    "900": "#...",
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "secondary": {
    "50": "#...",
    "100": "#...",
    "200": "#...",
    "300": "#...",
    "400": "#...",
    "500": "#...",
    "600": "#...",
    "700": "#...",
    "800": "#...",
    "900": "#...",
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "tertiary": {
    "50": "#...",
    "100": "#...",
    "200": "#...",
    "300": "#...",
    "400": "#...",
    "500": "#...",
    "600": "#...",
    "700": "#...",
    "800": "#...",
    "900": "#...",
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "error": {
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "warning": {
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "success": {
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "grey": {
    "50": "#...",
    "100": "#...",
    "200": "#...",
    "300": "#...",
    "400": "#...",
    "500": "#...",
    "600": "#...",
    "700": "#...",
    "800": "#...",
    "900": "#...",
    "A100": "#...",
    "A200": "#...",
    "A400": "#...",
    "A700": "#..."
  },
  "background": {
    "default": "#...",
    "surface": "#...",
    "paper": "#..."
  },
  "text": {
    "primary": "#...",
    "secondary": "#...",
    "inverse": "#...",
    "disabled": "rgba(...)"
  },
  "border": {
    "default": "#..."
  },
  "common": {
    "black": "#000000",
    "white": "#FFFFFF"
  },
  "info": {
    "light": "#...",
    "main": "#...",
    "dark": "#...",
    "contrastText": "#..."
  },
  "contrastThreshold": 3,
  "tonalOffset": 0.2,
  "divider": "rgba(...)",
  "action": {
    "active": "rgba(...)",
    "hover": "rgba(...)",
    "hoverOpacity": 0.04,
    "selected": "rgba(...)",
    "selectedOpacity": 0.08,
    "disabled": "rgba(...)",
    "disabledBackground": "rgba(...)",
    "disabledOpacity": 0.38,
    "focus": "rgba(...)",
    "focusOpacity": 0.12,
    "activatedOpacity": 0.12
  }
}

## Criterios de calidad
- `lightPalette` debe funcionar bien sobre fondos claros
- `darkPalette` debe funcionar bien sobre fondos oscuros
- `text.primary`, `text.secondary`, `divider`, `background`, `action` y `border` deben ajustarse correctamente al modo
- evita colores lavados o demasiado saturados si perjudican la legibilidad
- asegúrate de que `contrastText` sea correcto para botones y componentes de alto énfasis
- la salida debe verse como una paleta real de design system, no solo como variaciones aleatorias del color base

Ahora genera:
- una versión `lightPalette`
- una versión `darkPalette`

Usa:
- Color base principal: {COLOR_BASE}
- Formato de salida: {CON_TIPADO_O_SIN_TIPADO}
