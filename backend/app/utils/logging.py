"""Logging configuration"""

import logging
from app.config import settings


def configure_logging():
    """Configure application logging"""
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
