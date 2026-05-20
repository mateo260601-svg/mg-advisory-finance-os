from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROJECTS_DIR = DATA_DIR / "projects"
OUTPUTS_DIR = BASE_DIR / "outputs"
FRONTEND_DIR = BASE_DIR / "frontend"

APP_NAME = "MG Advisory Finance OS"
DEFAULT_LICENSE_KEY = "MG-ADVISORY-DEMO-2026"
LICENSE_KEY = os.getenv("MG_LICENSE_KEY", DEFAULT_LICENSE_KEY)

ALLOWED_UPLOAD_EXTENSIONS = {".pdf", ".xlsx", ".xlsm", ".csv"}
MAX_UPLOAD_BYTES = 50 * 1024 * 1024


def ensure_runtime_directories() -> None:
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
