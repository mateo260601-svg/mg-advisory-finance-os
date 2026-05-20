from fastapi import APIRouter


router = APIRouter(prefix="/api/decks", tags=["decks"])


@router.get("/status")
def deck_status():
    return {
        "status": "planned",
        "message": "PPTX/deck generation will be added as an optional builder.",
    }
