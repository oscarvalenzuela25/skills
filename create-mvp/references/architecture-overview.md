# Arquitectura inicial del MVP

## Objetivo

Convertir la especificación funcional, el modelo de dominio, las rutas y las decisiones de stack en una guía técnica coherente antes de crear tickets o código.

## Insumos

Leer completos PRD V2, ERD, Sitemap, Route Specs, restricciones de diseño y los tres documentos de stack. Señalar cualquier contradicción antes de redactar.

## Estructura del entregable

1. Contexto y límites del sistema.
2. Principios y restricciones arquitectónicas.
3. Componentes principales y responsabilidades.
4. Módulos funcionales y ownership.
5. Flujo de datos y contratos entre capas.
6. Autenticación, autorización y tratamiento de datos sensibles.
7. Persistencia, archivos, cache y procesos asíncronos cuando apliquen.
8. Estrategia frontend y navegación.
9. Estrategia backend y API.
10. Entornos, despliegue y configuración.
11. Observabilidad, seguridad y recuperación mínima.
12. Estrategia de pruebas.
13. Riesgos, decisiones provisionales y preguntas abiertas.
14. ADR que conviene crear antes o durante la implementación.

Mantener el diseño proporcional al MVP. No convertir decisiones futuras en infraestructura inmediata. Crear un ADR dentro de `docs/architecture/decisions/` cuando una decisión sea costosa de revertir, tenga alternativas relevantes o afecte varias partes del sistema.
