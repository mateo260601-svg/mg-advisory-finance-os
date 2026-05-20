from fastapi import APIRouter, HTTPException

from app.services.ai_service import claude_status, generate_project_brief
from app.services.financial_mapping_service import load_normalized_financials
from app.services.project_service import get_project


router = APIRouter(prefix="/api/ai", tags=["ai"])


@router.get("/status")
def ai_status():
    return claude_status()


@router.post("/projects/{project_id}/brief")
def ai_project_brief(project_id: str):
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    financials = load_normalized_financials(project_id)
    return generate_project_brief(project, financials)

