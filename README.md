# Food Store

A full-stack e-commerce platform for food delivery built with modern technologies.

## Project Structure

```
.
├── backend/           # FastAPI backend (Python)
├── frontend/          # React + Vite frontend (TypeScript)
├── docs/             # Project documentation
└── openspec/         # SDD (Spec-Driven Development) artifacts
    └── changes/      # Feature changes with specs and designs
```

## Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Backend runs on `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`

## Documentation

- [Backend Documentation](backend/README.md) - FastAPI setup and structure
- [Frontend Documentation](frontend/README.md) - React + Vite architecture
- [Project Description](docs/Descripcion.txt) - System overview and requirements
- [User Stories](docs/Historias_de_usuario.txt) - Feature specifications
- [Change Map](docs/CHANGES.md) - Development roadmap using SDD

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL + SQLModel ORM
- **Authentication**: JWT with refresh tokens
- **Payments**: MercadoPago integration

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **State Management**: Zustand + TanStack Query
- **Styling**: Tailwind CSS
- **Form Handling**: TanStack Form

## Development Workflow

This project uses **Spec-Driven Development (SDD)**. Every feature is built through:

1. **Propose** → Define what and why
2. **Design** → Plan architecture
3. **Implement** → Execute tasks
4. **Verify** → Validate against specs
5. **Archive** → Document and move forward

See `docs/CHANGES.md` for the complete roadmap.

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

Each change follows the SDD workflow. Changes are tracked in `openspec/changes/`.

## License

MIT
