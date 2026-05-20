from fastapi import APIRouter


router = APIRouter(prefix="/api/qoe", tags=["qoe"])


@router.get("/status")
def qoe_status():
    return {
        "status": "planned",
        "message": "QoE pack engine placeholder is available and isolated.",
    }
