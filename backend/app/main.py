"""FastAPI application factory and routes"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.middleware.error_handler import setup_error_handlers
from app.utils.logging import configure_logging
from app.routers import users, products, orders

# Configure logging
configure_logging()


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Error handlers
    setup_error_handlers(app)

    # Include routers
    app.include_router(users.router)
    app.include_router(products.router)
    app.include_router(orders.router)

    # Health check endpoint
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return {"status": "ok"}

    # Swagger UI
    @app.get("/docs")
    async def swagger_ui():
        """Swagger UI documentation"""
        return {"message": "Visit /docs for Swagger UI"}

    return app


# Create app instance
app = create_app()
