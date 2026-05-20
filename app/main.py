from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.config import APP_NAME, FRONTEND_DIR, ensure_runtime_directories


def create_app() -> FastAPI:
    ensure_runtime_directories()

    app = FastAPI(title=APP_NAME, version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_routes(app)

    if FRONTEND_DIR.exists():
        app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")

    @app.get("/", include_in_schema=False)
    def index():
        index_path = FRONTEND_DIR / "index.html"
        if index_path.exists():
            return FileResponse(index_path)
        return JSONResponse({"message": APP_NAME, "status": "frontend_missing"})

    @app.get("/health")
    def health():
        return {"status": "ok", "app": APP_NAME}

    return app


def register_routes(app: FastAPI) -> None:
    route_modules = [
        ("app.routes.auth", "router"),
        ("app.routes.projects", "router"),
        ("app.routes.upload", "router"),
        ("app.routes.bp", "router"),
        ("app.routes.debt", "router"),
        ("app.routes.qoe", "router"),
        ("app.routes.decks", "router"),
        ("app.routes.ai", "router"),
    ]

    for module_path, router_name in route_modules:
        try:
            module = __import__(module_path, fromlist=[router_name])
            app.include_router(getattr(module, router_name))
        except Exception as exc:
            @app.get(f"/system/route-load-errors/{module_path.split('.')[-1]}")
            def route_load_error(exc_message: str = str(exc), module_name: str = module_path):
                return {
                    "status": "degraded",
                    "module": module_name,
                    "error": exc_message,
                }


app = create_app()
