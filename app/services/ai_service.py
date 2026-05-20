import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-latest")


def claude_status() -> dict:
    return {
        "configured": bool(os.getenv("ANTHROPIC_API_KEY")),
        "model": DEFAULT_MODEL,
        "provider": "Anthropic Claude",
    }


def generate_project_brief(project: dict, financials: dict) -> dict:
    if not os.getenv("ANTHROPIC_API_KEY"):
        return {
            "configured": False,
            "brief": _fallback_brief(project, financials),
            "source": "local_fallback",
        }

    prompt = _project_prompt(project, financials)
    try:
        text = _call_claude(prompt)
        return {"configured": True, "brief": text, "source": "claude"}
    except Exception as exc:
        return {
            "configured": True,
            "brief": _fallback_brief(project, financials),
            "source": "local_fallback_after_error",
            "error": str(exc),
        }


def _call_claude(prompt: str) -> str:
    payload = {
        "model": DEFAULT_MODEL,
        "max_tokens": 1400,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": prompt}],
    }
    body = json.dumps(payload).encode("utf-8")
    request = Request(
        ANTHROPIC_API_URL,
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": os.getenv("ANTHROPIC_API_KEY", ""),
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Claude API HTTP {exc.code}: {detail[:500]}") from exc
    except URLError as exc:
        raise RuntimeError(f"Claude API network error: {exc.reason}") from exc

    content = data.get("content", [])
    text_parts = [part.get("text", "") for part in content if part.get("type") == "text"]
    return "\n".join(part for part in text_parts if part).strip()


def _project_prompt(project: dict, financials: dict) -> str:
    return (
        "You are an institutional finance advisor. Produce a concise Alvarez & Marsal / FTI style "
        "investment and restructuring briefing. Use professional finance language. Include: "
        "1) business snapshot, 2) historical financial observations, 3) debt/covenant considerations, "
        "4) key diligence questions, 5) recommended next analyses. Do not invent facts beyond the data.\n\n"
        f"Project:\n{json.dumps(project, indent=2)}\n\n"
        f"Normalized financials:\n{json.dumps(financials, indent=2)}"
    )


def _fallback_brief(project: dict, financials: dict) -> str:
    company = project.get("company_name", "Target Company")
    periods = ", ".join(financials.get("periods", [])) or "no historical periods loaded"
    sources = ", ".join(financials.get("source_files", [])) or "no source files"
    return (
        f"{company} preliminary finance brief.\n\n"
        f"Historical periods available: {periods}.\n"
        f"Source files: {sources}.\n\n"
        "Claude is not configured, so this is a local fallback. Recommended next steps: upload audited "
        "accounts, management accounts, trial balance, debt schedule and budget; validate mapping; then "
        "generate the BP model and covenant pack."
    )
