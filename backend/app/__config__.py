"""Backend configuration files"""

import os
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Requirements template for documentation
REQUIREMENTS = """fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlmodel==0.0.14
sqlalchemy==2.0.23
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
"""
