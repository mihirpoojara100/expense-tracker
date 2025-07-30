from contextlib import asynccontextmanager
from fastapi import FastAPI
from settings import settings
from app.routes.v1 import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI application."""
    # Startup
    print(f"🚀 Starting {settings.app_name} v{settings.app_version}")
    print(f"📊 Database URL: {settings.database_url}")
    print(f"🔧 Debug mode: {settings.debug}")

    # Yield control to the application
    yield

    # Shutdown
    print(f"🛑 Shutting down {settings.app_name}")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)

# Include the v1 API router with prefix
app.include_router(api_router, prefix="/v1")  # /api/v1
