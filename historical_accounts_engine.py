from fastapi import APIRouter, HTTPException

from app.schemas.project_schema import ProjectCreate
from app.services.project_service import create_project, get_project, list_projects


router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("")
def api_list_projects():
    return {"projects": list_projects()}


@router.post("")
def api_create_project(payload: ProjectCreate):
    project = create_project(payload)
    return {"project": project}


@router.get("/{project_id}")
def api_get_project(project_id: str):
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"project": project}

