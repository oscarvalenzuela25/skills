# Stack Backend — Referencia original

## Contenido

- Lenguaje, runtime, framework y arquitectura.
- API, autenticación y autorización.
- Datos, cache, jobs, búsqueda y storage.
- Observabilidad, seguridad y testing.
- Configuración, secretos y contenedores.

---

Necesito que en este apartado le hagas al usuario las consultas sobre que utilizara en la creación del proyecto, Por ejemplo deberás de consultar Lenguaje y darle las opciones que se tienen en los listados y si se te ocurre algo mas, mencionarlo para que pueda ser seleccionado.
Así con todos los títulos que se tienen y darle la opción del listado que conlleva cada titulo, literalmente es preguntarle para al al final llevar y crear un documento con el titulo de la sección y la respuesta del usuario, por ejemplo Lenguaje y la respuesta del usuario, si no sabe, guíalo y si no esta seguro, poner un por definir.

El documento que generaras se llamara "Stack Backend" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.
## Lenguaje

- TypeScript
- JavaScript
- Go
- Java
- Python

## Runtime / Plataforma

- Node.js
- Bun
- JVM
- Python runtime

## Framework Backend

- NestJS
- Express
- Fastify
- Hono
- Koa
- Django / FastAPI (Python)
- Spring Boot (Java)

## Arquitectura

- Monolito
- Modular monolith
- Microservicios
- Serverless (Functions)
- Event-driven

## API style

- REST
- GraphQL
- gRPC
- tRPC (TS end-to-end)

## Documentación de API

- OpenAPI / Swagger
- Redoc
- GraphQL schema + playground

## Autenticación

- JWT
- Sessions + cookies
- OAuth2 / OIDC
- SSO (SAML/OIDC)

## Autorización

- RBAC (roles)
- ABAC (políticas)
- Permissions por recurso
- Multi-tenant rules (por company/tenant)

## ORM / Acceso a datos

- Prisma
- TypeORM
- Sequelize
- Drizzle
- Mongoose (MongoDB)
- SQL nativo (pg)

## Base de datos principal

- PostgreSQL
- MySQL
- MongoDB
- SQL Server

## Migrations

- Prisma Migrate
- Flyway
- Liquibase
- dbmate
- Knex migrations

## Cache

- Redis
- Memcached
- Cache en memoria (solo casos simples)

## Mensajería / Async / Jobs

- BullMQ (Redis)
- RabbitMQ
- Kafka
- SQS
- Pub/Sub (GCP)
- Temporal (workflows)
- Cron jobs (scheduler)

## Search / Indexación (opcional)

- Elasticsearch
- OpenSearch
- Meilisearch
- Algolia

## Storage de archivos

- S3
- GCS
- Azure Blob
- Cloudinary (media)
- R2

## Email / Notificaciones

- SES
- SendGrid
- Mailgun
- Firebase Cloud Messaging (push)
- resend

## Payments (si aplica)

- Stripe
- Mercado Pago
- Adyen

## Observabilidad

- Logs: pino / winston
- Metrics: Prometheus
- Tracing: OpenTelemetry
- APM: Datadog / New Relic
- Error tracking: Sentry

## Validación / DTOs

- Zod
- Joi
- class-validator (Nest)

## Seguridad

- Helmet / security headers
- Rate limiting
- CORS (definido)
- CSRF (si sessions)
- Sanitización (inputs)
- Dependabot / Snyk

## Testing

- Unit: Jest
- Integration: Supertest
- E2E: Playwright (si toca flujos)
- Testcontainers (DB real)
- Contract tests (opcional)

## Config / Secrets

- dotenv
- AWS Secrets Manager
- GCP Secret Manager
- Vault
- Doppler

## Containerización

- Dockerfile
- Docker Compose (local)
