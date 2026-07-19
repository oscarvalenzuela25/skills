#!/usr/bin/env python3
"""Initialize the documentation scaffold for a create-mvp project."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys


DOCUMENTS = (
    ("01-interview.md", "Entrevista inicial", "Ninguna", "Responder la entrevista guiada y registrar hechos, inferencias y preguntas abiertas."),
    ("02-prd-v1.md", "PRD V1", "01-interview.md aprobado", "Transformar la entrevista en una primera definición funcional del MVP."),
    ("03-domain-model-erd.md", "Modelo de dominio ERD", "01-interview.md y 02-prd-v1.md aprobados", "Proponer y validar el modelo preliminar en DBML."),
    ("04-prd-v2.md", "PRD V2", "02-prd-v1.md y 03-domain-model-erd.md aprobados", "Reconciliar el PRD con el modelo de dominio."),
    ("05-sitemap.md", "Sitemap del MVP", "03-domain-model-erd.md y 04-prd-v2.md aprobados", "Definir únicamente las rutas necesarias para los flujos del MVP."),
    ("06-route-specs.md", "Route Specs", "03-domain-model-erd.md, 04-prd-v2.md y 05-sitemap.md aprobados", "Especificar cada ruta para que pueda implementarse sin inventar comportamiento."),
    ("07-design-constraints.md", "Restricciones de diseño", "05-sitemap.md y 06-route-specs.md aprobados", "Definir sistema visual, accesibilidad y restricciones de interacción aplicables."),
    ("08-stack-frontend.md", "Stack Frontend", "04-prd-v2.md, 06-route-specs.md y 07-design-constraints.md suficientes", "Seleccionar solo las herramientas frontend necesarias y dejar explícitos los pendientes."),
    ("09-stack-backend.md", "Stack Backend", "03-domain-model-erd.md, 04-prd-v2.md y 06-route-specs.md suficientes", "Seleccionar el stack backend coherente con dominio, reglas y contratos."),
    ("10-stack-devops.md", "Stack DevOps", "08-stack-frontend.md y 09-stack-backend.md definidos", "Definir repositorio, entornos, CI/CD, despliegue y operación mínima."),
    ("11-architecture-overview.md", "Arquitectura inicial", "Documentos funcionales y stacks aprobados", "Reconciliar componentes, datos, contratos, seguridad, pruebas y despliegue."),
    ("12-kanban.md", "Panel Kanban", "06-route-specs.md, stacks y 11-architecture-overview.md aprobados", "Derivar tickets trazables por ruta y trabajo transversal justificado."),
    ("13-readiness-review.md", "Revisión de preparación", "Todos los documentos anteriores revisados", "Comprobar coherencia y decidir si el MVP está listo para implementación."),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a non-destructive docs/mvp scaffold in a project directory."
    )
    parser.add_argument("--project-dir", required=True, help="Project directory to use or create")
    parser.add_argument("--name", help="Human-readable project name; defaults to directory name")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    return parser.parse_args()


def render(template: str, project_name: str) -> str:
    return (
        template.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{CREATED_DATE}}", date.today().isoformat())
    )


def document_stub(title: str, dependencies: str, next_action: str) -> str:
    return f"""# {title}

> Estado: pendiente
> Última actualización: {date.today().isoformat()}
> Dependencias: {dependencies}

## Objetivo

{next_action}

## Contenido

Pendiente de completar mediante el flujo guiado.

## Hechos confirmados

- Pendiente.

## Inferencias por validar

- Ninguna registrada.

## Preguntas abiertas

- Pendiente iniciar esta etapa.
"""


def main() -> int:
    args = parse_args()
    project_dir = Path(args.project_dir).expanduser().resolve(strict=False)
    if project_dir == Path(project_dir.anchor):
        print("Error: refusing to initialize a filesystem root.", file=sys.stderr)
        return 2
    if project_dir.exists() and not project_dir.is_dir():
        print(f"Error: target exists and is not a directory: {project_dir}", file=sys.stderr)
        return 2

    project_name = (args.name or project_dir.name).strip()
    if not project_name:
        print("Error: project name cannot be empty.", file=sys.stderr)
        return 2

    skill_dir = Path(__file__).resolve().parents[1]
    template_root = skill_dir / "assets" / "project-spec"
    template_files = (
        (template_root / "AGENTS.md", project_dir / "AGENTS.md"),
        (template_root / "docs" / "mvp" / "README.md", project_dir / "docs" / "mvp" / "README.md"),
        (template_root / "docs" / "mvp" / "00-progress.md", project_dir / "docs" / "mvp" / "00-progress.md"),
        (
            template_root / "docs" / "architecture" / "decisions" / "ADR-template.md",
            project_dir / "docs" / "architecture" / "decisions" / "ADR-template.md",
        ),
    )

    actions: list[tuple[Path, str]] = []
    for source, destination in template_files:
        if not source.is_file():
            print(f"Error: missing skill asset: {source}", file=sys.stderr)
            return 2
        if destination.exists():
            actions.append((destination, "skip"))
        else:
            actions.append((destination, render(source.read_text(encoding="utf-8"), project_name)))

    docs_dir = project_dir / "docs" / "mvp"
    for filename, title, dependencies, next_action in DOCUMENTS:
        destination = docs_dir / filename
        if destination.exists():
            actions.append((destination, "skip"))
        else:
            actions.append((destination, document_stub(title, dependencies, next_action)))

    verb = "WOULD CREATE" if args.dry_run else "CREATED"
    for destination, content in actions:
        if content == "skip":
            print(f"SKIPPED existing: {destination}")
            continue
        if args.dry_run:
            print(f"{verb}: {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        print(f"{verb}: {destination}")

    if args.dry_run:
        print(f"Dry run complete for: {project_dir}")
    else:
        print(f"Project specification initialized: {project_dir}")
        print(f"Next document: {docs_dir / '01-interview.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
