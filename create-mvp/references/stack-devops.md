# Stack DevOps — Referencia original

## Contenido

- Repositorio, ramas, CI y CD.
- Infraestructura, contenedores e IaC.
- Entornos, secretos y observabilidad.
- Networking, seguridad y políticas.
- Datos, releases y performance.

---

Necesito que en este apartado le hagas al usuario las consultas sobre que utilizara en la creación del proyecto, Por ejemplo deberás de consultar Repos y versionado y darle las opciones que se tienen en los listados y si se te ocurre algo mas, mencionarlo para que pueda ser seleccionado.
Así con todos los títulos que se tienen y darle la opción del listado que conlleva cada titulo, literalmente es preguntarle para al al final llevar y crear un documento con el titulo de la sección y la respuesta del usuario, por ejemplo Repos y versionado y la respuesta del usuario, si no sabe, guíalo y si no esta seguro, poner un por definir.

El documento que generaras se llamara "Stack DevOps" dentro de la carpeta del proyecto, si ya existe un documento con este nombre, reemplaza el contenido que tiene.
## Repos y versionado

- GitHub
- GitLab
- Bitbucket

## Estrategia de ramas

- Trunk-based
- GitFlow
- Release branches (si aplica)

## CI

- GitHub Actions
- GitLab CI
- CircleCI
- Jenkins (legacy)

## CD / Deploy

- GitHub Actions deploy
- Argo CD (GitOps)
- Flux CD
- Spinnaker

## Infraestructura (dónde corre)

- Vercel / Netlify (frontend)
- AWS (ECS / EKS / Lambda)
- GCP (Cloud Run / GKE / Functions)
- Azure (App Service / AKS)
- On-prem (raro)

## Container runtime

- Docker
- containerd

## Orquestación (si aplica)

- Kubernetes (EKS/GKE/AKS)
- ECS
- Nomad

## IaC (Infrastructure as Code)

- Terraform
- Pulumi
- AWS CDK
- CloudFormation
- Helm (K8s)

## Entornos

- Local
- Dev
- Staging
- Prod
- Preview environments (por PR)

## Secrets management

- GitHub Secrets
- AWS Secrets Manager
- GCP Secret Manager
- Vault
- Doppler

## Observabilidad

- Logs: ELK / OpenSearch, Loki
- Metrics: Prometheus + Grafana
- Tracing: OpenTelemetry + Jaeger/Tempo
- APM: Datadog / New Relic
- Error tracking: Sentry

## Monitoreo / Alertas

- Grafana Alerting
- Datadog monitors
- PagerDuty / Opsgenie
- Slack alerts

## Networking

- DNS: Route53 / Cloudflare DNS
- CDN: Cloudflare / CloudFront / Fastly
- Load balancer: ALB/NLB / Ingress NGINX
- WAF: Cloudflare WAF / AWS WAF
- TLS/SSL: ACM / Let’s Encrypt

## Seguridad (DevSecOps)

- SAST: CodeQL / SonarQube / Deepsource
- Dependency scan: Dependabot / Snyk
- Secret scan: Gitleaks
- Container scan: Trivy
- SBOM: Syft/Grype

## Calidad / Policies

- Branch protection rules
- Required reviews
- Required status checks
- Conventional commits
- Semantic versioning

## Artefactos / Registry

- Docker Hub
- GHCR (GitHub Container Registry)
- ECR (AWS)
- GCR/Artifact Registry (GCP)

## Bases de datos (operación)

- Backups automáticos
- Point-in-time recovery (PITR)
- Migrations en pipeline
- Read replicas (si aplica)

## Release / Rollback

- Blue/Green
- Canary releases
- Feature flags (para rollout)
- Rollback automático

## Performance / Edge

- Edge functions (Vercel/Cloudflare)
- Caching rules
- Image optimization pipeline
