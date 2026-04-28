# Design: infrastructure-setup

## Technical Architecture

### Backend Structure (FastAPI)

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada, FastAPI app instance
│   ├── config.py               # Configuración centralizada (settings, env vars)
│   ├── routers/
│   │   ├── __init__.py
│   │   └── _template.py        # Template para routers futuros
│   ├── services/
│   │   ├── __init__.py
│   │   └── _template.py        # Template para services futuros
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── _base.py            # BaseRepository placeholder
│   ├── models/
│   │   ├── __init__.py
│   │   └── _template.py        # Template para models futuros
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── _template.py        # Template para schemas Pydantic
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── error_handler.py    # Manejo centralizado de errores (RFC 7807)
│   └── utils/
│       ├── __init__.py
│       └── logging.py          # Configuración de logging
├── requirements.txt            # Dependencias Python con versiones pinned
├── .env.example               # Variables de entorno necesarias
└── README.md                  # Instrucciones setup backend

Frontend Structure (React + Vite)

frontend/
├── src/
│   ├── app/
│   │   ├── App.tsx            # Root component
│   │   ├── providers.tsx       # Providers (TanStack Query, Zustand, etc)
│   │   └── index.css          # Estilos globales
│   ├── pages/
│   │   ├── _template.tsx      # Template para nuevas páginas
│   │   └── NotFound.tsx       # Página 404
│   ├── widgets/
│   │   └── _template.tsx      # Template para widgets
│   ├── features/
│   │   └── _template.tsx      # Template para features
│   ├── entities/
│   │   └── _template.tsx      # Template para entities
│   ├── shared/
│   │   ├── ui/
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   └── _template.tsx
│   │   ├── hooks/
│   │   │   ├── _template.ts
│   │   │   └── index.ts
│   │   ├── types/
│   │   │   ├── api.ts
│   │   │   └── common.ts
│   │   ├── config/
│   │   │   └── axios.ts       # Axios instance + interceptors
│   │   ├── utils/
│   │   │   ├── _template.ts
│   │   │   └── index.ts
│   │   └── constants/
│   │       └── index.ts
│   ├── main.tsx               # Entry point
│   └── vite-env.d.ts         # Tipos de Vite
├── public/                    # Assets estáticos
├── vite.config.ts            # Configuración Vite
├── tsconfig.json             # Configuración TypeScript estricta
├── tailwind.config.ts        # Configuración Tailwind
├── postcss.config.cjs        # Configuración PostCSS
├── package.json              # Dependencias npm
├── .env.example              # Variables de entorno
└── README.md                 # Instrucciones setup frontend

Project Root

.
├── backend/                   # Código FastAPI
├── frontend/                  # Código React + Vite
├── docs/                      # Documentación del sistema (ya existe)
├── .gitignore                # Patrones de exclusión
├── Makefile                   # Scripts de conveniencia
└── README.md                  # Instrucciones generales
```

## Configuration Details

### Backend Configuration (app/config.py)

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    app_name: str = "Food Store API"
    debug: bool = False
    version: str = "0.1.0"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS
    allowed_origins: list = ["http://localhost:5173"]
    
    # Database (placeholder - setup real en database-design-migrations)
    database_url: str = "postgresql://user:password@localhost/foodstore"
    
    # JWT (placeholder - setup real en auth-backend-jwt)
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

### Frontend vite.config.ts

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
```

### Frontend tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "strict": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## Dependencies

### Backend (requirements.txt - selección crítica)

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlmodel==0.0.14
sqlalchemy==2.0.23
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
```

(Más dependencias se agregarán en cambios posteriores: alembic, slowapi, requests, etc.)

### Frontend (package.json - selección crítica)

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^5.3.3",
    "@tanstack/react-query": "^5.28.0",
    "@tanstack/react-form": "^0.16.0",
    "zustand": "^4.4.7",
    "axios": "^1.6.2",
    "tailwindcss": "^3.4.0"
  },
  "devDependencies": {
    "vite": "^5.0.8",
    "@vitejs/plugin-react": "^4.2.1",
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "postcss": "^8.4.32",
    "autoprefixer": "^10.4.16"
  }
}
```

## Development Workflow

### Backend
```bash
# Setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Desarrollo
python main.py
# O con auto-reload:
# uvicorn app.main:app --reload

# Test
pytest
```

### Frontend
```bash
# Setup
cd frontend
npm install

# Desarrollo
npm run dev

# Build
npm run build

# Preview build
npm run preview

# Lint
npm run lint

# Format
npm run format
```

## Module Organization

Todos los módulos futuros siguen este patrón:

```
app/
├── routers/
│   └── router_<modulo>.py      # Endpoint definitions
├── services/
│   └── service_<modulo>.py     # Business logic
├── repositories/
│   └── repository_<modulo>.py  # Data access
├── models/
│   └── model_<modulo>.py       # DB models
└── schemas/
    └── schema_<modulo>.py      # Pydantic schemas
```

Cada módulo sigue flujo: Router → Service → Repository → Model

## Error Handling (RFC 7807)

El middleware centralizado en `app/middleware/error_handler.py` captura excepciones y devuelve respuestas en formato Problem Details:

```json
{
  "type": "https://api.foodstore.com/errors/validation",
  "title": "Validation Error",
  "status": 400,
  "detail": "Email field is required",
  "instance": "/api/v1/auth/register"
}
```

## Success Checks

Después de implementar este change:

1. ✅ Estructura de carpetas exists y es consistente
2. ✅ `pip install -r requirements.txt` instala sin error
3. ✅ `npm install` instala sin error
4. ✅ `python main.py` inicia en 8000
5. ✅ `npm run dev` inicia en 5173
6. ✅ Vite proxy a backend funciona (`http://localhost:5173/api` → `http://localhost:8000/api`)
7. ✅ `npm run build` genera `frontend/dist/`
8. ✅ TypeScript no reporta errores en archivos de template vacíos
