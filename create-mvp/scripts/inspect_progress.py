#!/usr/bin/env python3
"""Inspect create-mvp progress without modifying the project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


DOCUMENTS = (
    (1, "01-interview.md", "Entrevista"),
    (2, "02-prd-v1.md", "PRD V1"),
    (3, "03-domain-model-erd.md", "Modelo de dominio ERD"),
    (4, "04-prd-v2.md", "PRD V2"),
    (5, "05-sitemap.md", "Sitemap"),
    (6, "06-route-specs.md", "Route Specs"),
    (7, "07-design-constraints.md", "Restricciones de diseño"),
    (8, "08-stack-frontend.md", "Stack Frontend"),
    (9, "09-stack-backend.md", "Stack Backend"),
    (10, "10-stack-devops.md", "Stack DevOps"),
    (11, "11-architecture-overview.md", "Arquitectura inicial"),
    (12, "12-kanban.md", "Kanban"),
    (13, "13-readiness-review.md", "Revisión de preparación"),
)

APPROVED_STATES = {"aprobado", "no aplica"}
STATUS_RE = re.compile(r"^> Estado:\s*(.+?)\s*$", re.MULTILINE | re.IGNORECASE)
CHECK_RE = re.compile(r"^- \[([ xX])\]\s*(\d{2})\.", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report create-mvp project progress")
    parser.add_argument("project_dir", help="Initialized project directory")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_dir = Path(args.project_dir).expanduser().resolve(strict=False)
    docs_dir = project_dir / "docs" / "mvp"
    progress_file = docs_dir / "00-progress.md"

    if not progress_file.is_file():
        print(f"Not initialized: {progress_file} does not exist", file=sys.stderr)
        return 2

    progress_text = progress_file.read_text(encoding="utf-8")
    checked = {int(step): mark.lower() == "x" for mark, step in CHECK_RE.findall(progress_text)}
    items = []
    warnings = []
    next_step = None

    for number, filename, label in DOCUMENTS:
        path = docs_dir / filename
        exists = path.is_file()
        status = "faltante"
        if exists:
            text = path.read_text(encoding="utf-8")
            match = STATUS_RE.search(text)
            status = match.group(1).strip().lower() if match else "sin estado"

        is_checked = checked.get(number, False)
        is_approved = status in APPROVED_STATES
        if is_checked and not is_approved:
            warnings.append(f"Paso {number:02d}: checklist marcado pero documento está '{status}'.")
        if is_approved and not is_checked:
            warnings.append(f"Paso {number:02d}: documento está '{status}' pero checklist no está marcado.")
        if next_step is None and not (is_checked and is_approved):
            next_step = {"number": number, "file": str(path), "label": label, "status": status}

        items.append(
            {
                "number": number,
                "label": label,
                "file": str(path),
                "exists": exists,
                "status": status,
                "checked": is_checked,
            }
        )

    result = {
        "project": str(project_dir),
        "initialized": True,
        "complete": next_step is None,
        "next_step": next_step,
        "items": items,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"Project: {project_dir}")
    for item in items:
        mark = "x" if item["checked"] else " "
        print(f"[{mark}] {item['number']:02d} {item['label']}: {item['status']}")
    if next_step:
        print(
            f"Next: {next_step['number']:02d} {next_step['label']} "
            f"({next_step['status']}) — {next_step['file']}"
        )
    else:
        print("All create-mvp steps are approved.")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
