# Change: infrastructure-setup

## Executive Summary

Establecer la base técnica del proyecto Food Store: estructura de carpetas, dependencias core, configuración de herramientas de desarrollo, y setup inicial de backend (FastAPI) y frontend (React + Vite). Este change NO incluye código de negocio — solo infraestructura y tooling que permite que los cambios posteriores se construyan sobre una base sólida.

## Problem Statement

Sin infraestructura base:
- No hay estructura clara para organizar código
- No hay herramientas configuradas (linters, formatters, build tools)
- No hay forma de desarrollar o testear nada
- Cada desarrollador puede tomar decisiones diferentes sobre la estructura

## Solution Overview

### Backend (FastAPI)
- Estructura en capas: `app/routers/`, `app/services/`, `app/repositories/`, `app/models/`
- Configuración centralizada en `app/config.py` (variables de entorno, CORS, logging)
- Punto de entrada en `main.py`
- Dependencias en `requirements.txt` con versiones pinned
- Setup de `uvicorn` para desarrollo local

### Frontend (React + TypeScript + Vite)
- Estructura Feature-Sliced Design: `src/app/`, `src/pages/`, `src/widgets/`, `src/features/`, `src/entities/`, `src/shared/`
- Configuración Vite en `vite.config.ts`
- Tailwind CSS preconfigurado
- TypeScript stricto habilitado
- `package.json` con todas las dependencias core

### Raíz del proyecto
- `.gitignore` robusto (node_modules, __pycache__, .env, build outputs)
- `.env.example` documentando variables de entorno necesarias
- `README.md` con instrucciones para setup local
- Scripts en `Makefile` o `package.json` para comandos comunes

## Why This Approach

- **Estándar**: La estructura propuesta es la best practice para FastAPI + React
- **Escalable**: Cada cambio posterior es una carpeta nueva dentro de la estructura base
- **Independencia**: Backend y frontend pueden desarrollarse en paralelo
- **Developer Experience**: Setup local funciona con un comando (`make dev` o similar)

## Scope & Exclusions

### ✅ Incluye
- Estructura de carpetas backend y frontend
- Configuración de herramientas (Vite, TypeScript, Tailwind)
- Setup de dependencias (requirements.txt, package.json)
- Archivos de configuración (.gitignore, .env.example)
- README con instrucciones de desarrollo
- Scripts de conveniencia para dev local

### ❌ Excluye
- Modelos de base de datos (en `database-design-migrations`)
- Código de autenticación (en `auth-backend-jwt`)
- Componentes React (en `frontend-core-setup`)
- Endpoints de API específicos

## Success Criteria

- ✅ El repositorio tiene estructura clara y consistente
- ✅ Se puede ejecutar `pip install -r requirements.txt` + `npm install` sin errores
- ✅ `python main.py` inicia servidor FastAPI en localhost:8000
- ✅ `npm run dev` inicia servidor Vite en localhost:5173
- ✅ `npm run build` genera build de producción sin errores
- ✅ TypeScript stricto no reporta errores en archivos vacíos de la estructura

## Related User Stories

- US-000: Setup inicial del proyecto
- US-000a: Configuración de herramientas de desarrollo
- US-000c: Configuración de frontend

## Dependencies

Ninguno. Este es el primer change.

## Effort Estimation

**2 puntos** (~4-6 horas de trabajo)
- Estructura: ~1 hora
- Dependencias y configuración: ~2 horas
- Tests de que todo está conectado: ~1-2 horas
