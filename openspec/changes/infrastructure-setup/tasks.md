# Tasks: infrastructure-setup

## Implementation Checklist

### Task 1: Crear estructura de carpetas backend
- [x] Crear `backend/app/` con estructura descrita en design.md
- [x] Crear `backend/app/routers/`
- [x] Crear `backend/app/services/`
- [x] Crear `backend/app/repositories/`
- [x] Crear `backend/app/models/`
- [x] Crear `backend/app/schemas/`
- [x] Crear `backend/app/middleware/`
- [x] Crear `backend/app/utils/`
- [x] Crear archivo `backend/app/__init__.py`
- [x] Crear archivo `backend/app/main.py` (FastAPI instance + health check)
- [x] Crear archivo `backend/app/config.py` con clase Settings
- [x] Crear archivo `backend/app/middleware/error_handler.py` (RFC 7807 handlers)
- [x] Crear archivo `backend/app/utils/logging.py` (logging configuration)

**Effort**: ~30 minutos  
**Verification**: `tree backend/` muestra la estructura completa

---

### Task 2: Crear estructura de carpetas frontend (FSD)
- [x] Crear `frontend/src/app/`
- [x] Crear `frontend/src/pages/`
- [x] Crear `frontend/src/widgets/`
- [x] Crear `frontend/src/features/`
- [x] Crear `frontend/src/entities/`
- [x] Crear `frontend/src/shared/ui/`
- [x] Crear `frontend/src/shared/hooks/`
- [x] Crear `frontend/src/shared/types/`
- [x] Crear `frontend/src/shared/config/`
- [x] Crear `frontend/src/shared/utils/`
- [x] Crear `frontend/src/shared/constants/`
- [x] Crear archivo `frontend/src/main.tsx` (entry point con React.StrictMode)
- [x] Crear archivo `frontend/src/app/App.tsx` (root component con welcome)
- [x] Crear archivo `frontend/src/app/providers.tsx` (QueryClientProvider)
- [x] Crear archivo `frontend/src/vite-env.d.ts` (Vite types)

**Effort**: ~30 minutos  
**Verification**: `tree frontend/src/` muestra estructura FSD completa

---

### Task 3: Configurar Backend (FastAPI + Uvicorn)
- [x] Crear `backend/requirements.txt` con dependencias core
- [x] Crear `backend/.env.example` con variables de entorno
- [x] Crear `backend/README.md` con instrucciones setup
- [x] Crear `backend/main.py` que importe `app` y corre con uvicorn
- [x] Configurar app/main.py con FastAPI instance básica
- [x] Agregar CORS middleware a la app
- [x] Agregar error handler middleware (RFC 7807)
- [x] Agregar endpoint de health check: `GET /health` que devuelva `{"status": "ok"}`
- [x] Probar que `python main.py` inicia sin errores
- [x] Crear routers para users, products, orders con endpoints stubs

**Effort**: ~1 hora  
**Verification**: `curl http://localhost:8000/health` devuelve status 200 + JSON

---

### Task 4: Configurar Frontend (React + Vite + TypeScript)
- [x] Crear `frontend/vite.config.ts` con configuración estándar
- [x] Crear `frontend/tsconfig.json` con strict mode habilitado
- [x] Crear `frontend/tsconfig.node.json` para build tools
- [x] Crear `frontend/tailwind.config.ts`
- [x] Crear `frontend/postcss.config.cjs`
- [x] Crear `frontend/package.json` con scripts y dependencias
- [x] Crear `frontend/.env.example` con variables de entorno (VITE_API_URL)
- [x] Crear `frontend/README.md` con instrucciones setup
- [x] Implementar `src/shared/config/axios.ts` básico (sin interceptores aún)
- [x] Implementar `src/app/providers.tsx` con QueryClientProvider
- [x] Implementar `src/app/App.tsx` con router placeholder
- [x] Implementar `src/app/index.css` con Tailwind directives (@tailwind...)
- [x] Implementar `src/main.tsx` con React.StrictMode + App
- [x] Probar que `npm install` funciona sin errores
- [x] Probar que `npm run dev` inicia sin errores
- [x] Probar que `npm run build` compila TypeScript sin errores

**Effort**: ~1.5 horas  
**Verification**: `npm run dev` arranca en puerto 5173, browser abre sin errores

---

### Task 5: Configurar Git (.gitignore, etc)
- [x] Crear/actualizar `.gitignore` en raíz con:
  - Python: `__pycache__`, `.venv`, `*.egg-info`, `.pytest_cache`
  - Node: `node_modules`, `dist`, `.eslintcache`
  - IDE: `.vscode`, `.idea`, `*.swp`, `.DS_Store`
  - Env: `.env`, `.env.local`, `.env.*.local`
- [x] Crear/actualizar `.env.example` en raíz (y en backend y frontend por separado)
- [x] Crear `README.md` en raíz con instrucciones generales
- [x] Verificar que `.gitignore` excluye correctamente (check con `git status`)

**Effort**: ~20 minutos  
**Verification**: `git status` no muestra archivos que deberían estar ignorados

---

### Task 6: Crear scripts de conveniencia (Makefile)
- [x] Crear `Makefile` en raíz con targets útiles:
  - Target `make setup`: instala backend y frontend
  - Target `make dev`: arranca backend y frontend simultáneamente
  - Target `make format`: formatea código (backend + frontend)
  - Target `make lint`: linters (backend + frontend)
  - Target `make clean`: limpia build artifacts
- [x] Verificar que Makefile tiene sintaxis correcta

**Effort**: ~30 minutos  
**Verification**: `make setup` completa sin errores

---

### Task 7: Verificación final
- [x] Ejecutar `python backend/main.py`
  - [x] Debe arrancar sin errores
  - [x] `curl http://localhost:8000/health` devuelve 200 + `{"status": "ok"}`
  - [x] `curl http://localhost:8000/docs` devuelve Swagger UI
  - [x] Backend app imports successfully with 21 routes configured
- [x] Ejecutar `cd frontend && npm run dev`
  - [x] Debe arrancar en puerto 5173 sin errores
  - [x] Browser abre automáticamente
  - [x] No hay errores de TypeScript
  - [x] Detener con Ctrl+C
- [x] Ejecutar `cd frontend && npm run build`
  - [x] Build completa sin errores
  - [x] Genera carpeta `frontend/dist/`
- [x] Verificar que git status muestra solo cambios esperados
- [x] Documentar en README cualquier paso manual si es necesario

**Effort**: ~30 minutos  
**Verification**: Todos los pasos anteriores pasan sin error

---

## Total Effort

**~4-5 horas** (2 puntos de complejidad)

## Dependencies Between Tasks

- Task 1 (Backend dirs) es independiente
- Task 2 (Frontend dirs) es independiente
- Task 3 depende de Task 1
- Task 4 depende de Task 2
- Task 5 es independiente
- Task 6 es independiente
- Task 7 depende de Task 3 y 4

**Parallelizable**: Tasks 1, 2, 5, 6 pueden hacerse simultáneamente

## Verification After Completion

Checklist final para saber que este change está 100% listo:

✅ Backend
- [x] `python backend/main.py` arranca en puerto 8000
- [x] `GET /health` devuelve 200
- [x] `GET /docs` muestra Swagger UI
- [x] `pip install -r backend/requirements.txt` sin errores
- [x] Routers users/products/orders creados e integrados

✅ Frontend
- [x] `npm install` sin errores
- [x] `npm run dev` arranca en puerto 5173
- [x] `npm run build` genera `dist/`
- [x] No hay errores TypeScript

✅ General
- [x] `.gitignore` funciona correctamente
- [x] `git status` es limpio (solo nuevos archivos esperados)
- [x] README.md documenta pasos para levantar ambiente
- [x] Estructura de carpetas matchea design.md
