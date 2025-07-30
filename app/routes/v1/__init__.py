from fastapi import APIRouter

# Create the main v1 API router
api_router = APIRouter()


# Root endpoint for v1 API
@api_router.get("/")
async def root():
    """Root endpoint for the v1 API."""
    return {
        "message": "Expense Tracker API v1",
        "version": "v1.0.0",
        "endpoints": {
            "users": "/users",
        },
        "documentation": "/docs",
        "openapi": "/openapi.json",
    }


# Health check endpoint
@api_router.get("/health")
async def health_check():
    """Health check endpoint for the API."""
    return {
        "status": "healthy",
        "version": "v1",
        "message": "Expense Tracker API is running",
    }
