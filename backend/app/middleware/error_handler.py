"""Error handling middleware (RFC 7807 - Problem Details for HTTP APIs)"""

import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

logger = logging.getLogger(__name__)


async def http_exception_handler(request: Request, exc: Exception):
    """Handle HTTP exceptions and return RFC 7807 Problem Details"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "type": "https://api.foodstore.com/errors/internal-error",
            "title": "Internal Server Error",
            "status": 500,
            "detail": "An unexpected error occurred",
            "instance": str(request.url),
        },
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors and return RFC 7807 Problem Details"""
    errors = exc.errors()
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "type": "https://api.foodstore.com/errors/validation-error",
            "title": "Validation Error",
            "status": 422,
            "detail": "One or more validation errors occurred",
            "instance": str(request.url),
            "errors": errors,
        },
    )


def setup_error_handlers(app: FastAPI):
    """Register error handlers with FastAPI application"""
    app.add_exception_handler(Exception, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
