from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .config import get_settings
from .main import main as run_main_logic


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None]:
    """
    Lifecycle manager for the FastAPI app.
    Startup and Shutdown logic goes here.
    """
    # Startup logic
    settings = get_settings()
    print(f"Starting {settings.PROJECT_NAME} in {settings.ENVIRONMENT} mode...")

    yield

    # Shutdown logic
    print(f"Shutting down {settings.PROJECT_NAME}...")


def create_app() -> FastAPI:
    """Factory function to create the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        lifespan=lifespan,
        docs_url=None,
        redoc_url=None,
    )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        _request: Request, exc: Exception
    ) -> JSONResponse:
        """Global exception handler to return consistent JSON errors."""
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error", "error": str(exc)},
        )

    @app.get("/health")
    async def health_check() -> dict[str, str]:
        """Health check endpoint for probes."""
        return {"status": "ok", "version": settings.VERSION}

    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint example."""
        return {"message": f"Hello from {settings.PROJECT_NAME} API"}

    @app.get("/run")
    async def trigger_run() -> dict[str, str]:
        """Trigger the main logic via API."""
        run_main_logic()
        return {"status": "Main logic executed"}

    return app


app = create_app()
