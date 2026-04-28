# Food Store Backend Setup

## Prerequisites

- Python 3.11+
- PostgreSQL 14+

## Installation

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Server

With auto-reload (development):
```bash
python main.py
```

Production:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI spec: http://localhost:8000/openapi.json

## Testing

```bash
pytest
```

## Project Structure

- `app/` - Application code
  - `routers/` - API endpoints
  - `services/` - Business logic
  - `repositories/` - Data access layer
  - `models/` - Database models
  - `schemas/` - Pydantic validation schemas
  - `middleware/` - Request/response middleware
  - `utils/` - Utility functions
  - `config.py` - Settings and configuration
  - `main.py` - FastAPI application factory
- `requirements.txt` - Python dependencies
- `main.py` - Entry point
