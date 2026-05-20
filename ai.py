from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4

from app.config import PROJECTS_DIR
from app.schemas.project_schema import ProjectCreate


def project_dir(project_id: str) -> Path:
    return PROJECTS_DIR / project_id


def project_metadata_path(project_id: str) -> Path:
    return project_dir(project_id) / "project.json"


def create_project(payload: ProjectCreate) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    project_id = uuid4().hex[:12]
    directory = project_dir(project_id)
    (directory / "documents").mkdir(parents=True, exist_ok=True)
    (directory / "normalized").mkdir(parents=True, exist_ok=True)

    project = {
        "id": project_id,
        "company_name": payload.company_name.strip(),
        "project_type": payload.project_type.strip(),
        "currency": payload.currency.strip().upper(),
        "fiscal_year_end": payload.fiscal_year_end.strip(),
        "created_at": now,
        "updated_at": now,
        "status": "active",
    }
    _write_json(project_metadata_path(project_id), project)
    return project


def list_projects() -> list[dict]:
    projects = []
    if not PROJECTS_DIR.exists():
        return projects
    for path in sorted(PROJECTS_DIR.glob("*/project.json")):
        try:
            projects.append(_read_json(path))
        except Exception:
            continue
    return sorted(projects, key=lambda item: item.get("created_at", ""), reverse=True)


def get_project(project_id: str) -> dict | None:
    path = project_metadata_path(project_id)
    if not path.exists():
        return None
    try:
        return _read_json(path)
    except Exception:
        return None


def touch_project(project_id: str) -> None:
    project = get_project(project_id)
    if not project:
        return
    project["updated_at"] = datetime.now(timezone.utc).isoformat()
    _write_json(project_metadata_path(project_id), project)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

