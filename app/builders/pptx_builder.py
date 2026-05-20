def build_deck_placeholder(project: dict) -> dict:
    """Placeholder for future PPTX deck generation."""
    return {
        "status": "planned",
        "company": project.get("company_name", ""),
        "message": "PPTX builder is not yet implemented.",
    }
