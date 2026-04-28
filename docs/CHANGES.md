# Food Store — Mapa de Changes (SDD)

## 📋 Introducción

Este documento describe la estrategia completa de desarrollo de Food Store usando **Spec-Driven Development (SDD)**. El proyecto se divide en **37 changes** ordenados lógicamente de principio a fin, formando un DAG (grafo acíclico dirigido) sin ciclos donde cada change solo depende de los anteriores.

Cada change es una unidad de trabajo completa que incluye:
- **proposal.md**: QUÉ se construye y POR QUÉ
- **design.md**: CÓMO técnicamente (arquitectura, APIs, modelos de datos)
- **tasks.md**: CHECKLIST atómico de implementación

---

## 🎯 Principios de Diseño de los Changes

1. **Granularidad**: Cada change es implementable en **1-2 días** (4-8 horas de trabajo)
2. **Cohesión**: Todos los artefactos de un change relatan la misma historia
3. **Dependencias lineales**: El orden es **crítico** — B no puede empezar sin que A esté archivado
4. **Independencia de features**: Cambios en features específicos no afectan otros cambios

---

## 🗺️ Mapa Completo de Changes — Orden de Desarrollo

### **Fase 1: Infraestructura Base (4 changes)**
Establece la capa base técnica en la que todo el sistema se construye.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 1 | `infrastructure-setup` | Repositorio, estructura base backend/frontend, dependencias | - | ⭐⭐ |
| 2 | `database-design-migrations` | ERD v5, PostgreSQL, Alembic, seed data | infrastructure-setup | ⭐⭐⭐ |
| 3 | `patterns-and-core-infrastructure` | BaseRepository, Unit of Work, dependencias FastAPI, RFC 7807 | database-design-migrations | ⭐⭐⭐ |
| 4 | `frontend-core-setup` | React + TypeScript + Vite + Tailwind, FSD, Axios, TanStack Query | infrastructure-setup | ⭐⭐ |

### **Fase 2: Autenticación y Autorización (6 changes)**
Implementa la seguridad base del sistema: autenticación JWT y RBAC.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 5 | `zustand-stores-setup` | authStore, cartStore, paymentStore, uiStore | frontend-core-setup | ⭐⭐ |
| 6 | `auth-backend-jwt` | Registro, login, refresh token rotativo, logout, rate limiting | patterns-and-core-infrastructure | ⭐⭐⭐ |
| 7 | `rbac-authorization` | Roles (ADMIN, STOCK, PEDIDOS, CLIENT), validación de permisos | auth-backend-jwt | ⭐⭐ |
| 8 | `auth-frontend-login-register` | Componentes login/register, integración authStore | auth-backend-jwt + zustand-stores-setup | ⭐⭐ |
| 9 | `token-refresh-frontend` | Interceptor Axios para refresh automático, caché de requests | auth-frontend-login-register | ⭐⭐ |
| 10 | `frontend-navigation-layout` | Navegación por rol, rutas privadas, sidebar, layout responsivo | rbac-authorization + auth-frontend-login-register | ⭐⭐ |

### **Fase 3: Catálogo de Productos (5 changes)**
Construye el catálogo que los clientes ven y los gestores administran.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 11 | `categories-backend` | CRUD categorías jerárquicas con CTE recursivo, soft delete | rbac-authorization | ⭐⭐⭐ |
| 12 | `ingredients-backend` | CRUD ingredientes con es_alergeno, M2M con productos | rbac-authorization | ⭐⭐ |
| 13 | `products-backend` | CRUD productos con precio NUMERIC, stock atómico, M2M categorías/ingredientes | categories-backend + ingredients-backend | ⭐⭐⭐ |
| 14 | `product-catalog-frontend` | Listado paginado, filtros (categoría, búsqueda, precio), vista detalle | products-backend + frontend-navigation-layout | ⭐⭐⭐ |
| 15 | `admin-stock-management` | Panel de stock: actualizar cantidades, cambiar disponibilidad | products-backend | ⭐⭐ |

### **Fase 4: Carrito y Dirección (3 changes)**
Prepara el contexto del usuario para checkout.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 16 | `directions-backend` | CRUD direcciones por usuario, dirección principal, validaciones | rbac-authorization | ⭐⭐ |
| 17 | `cart-management-frontend` | Carrito client-side + localStorage, agregar/remover/actualizar, personalización | zustand-stores-setup + product-catalog-frontend | ⭐⭐ |
| 18 | `user-profile-frontend` | Visualización/edición perfil, gestión de direcciones | auth-frontend-login-register + directions-backend | ⭐⭐ |

### **Fase 5: Pedidos y Máquina de Estados (4 changes)**
Implementa el núcleo operativo: creación de pedidos y control de ciclo de vida.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 19 | `orders-backend-core` | Creación atómica con Unit of Work, snapshots, detalle de pedido | products-backend + directions-backend | ⭐⭐⭐⭐ |
| 20 | `orders-state-machine-backend` | FSM, transiciones validadas, decremento/restauración stock atómica, historial | orders-backend-core | ⭐⭐⭐ |
| 21 | `orders-list-frontend` | Listado de pedidos cliente, filtros estado, vista detalle con historial | orders-backend-core + product-catalog-frontend | ⭐⭐ |
| 22 | `admin-orders-management` | Panel gestor pedidos: todos los pedidos, avance estados, historial, cancelación | orders-state-machine-backend | ⭐⭐ |

### **Fase 6: Pagos e Integración MercadoPago (3 changes)**
Cierra el flujo de compra con integración de pagos.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 23 | `payments-mercadopago-backend` | Integración Checkout API, idempotency_key, webhook IPN, actualización estado | orders-state-machine-backend | ⭐⭐⭐ |
| 24 | `checkout-payment-frontend` | Formulario checkout con SDK MercadoPago, selección dirección/forma pago | cart-management-frontend + payments-mercadopago-backend | ⭐⭐⭐ |
| 25 | `payment-status-frontend` | Estado de pago con polling, timeline de transiciones de pedido | checkout-payment-frontend + orders-state-machine-backend | ⭐⭐ |

### **Fase 7: Administración (5 changes)**
Herramientas para gestores y administradores.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 26 | `admin-users-management-backend` | CRUD usuarios, asignación roles, restricción último ADMIN, soft delete | rbac-authorization | ⭐⭐ |
| 27 | `admin-users-frontend` | Panel admin users: CRUD, asignación roles, lista con filtros | admin-users-management-backend + rbac-authorization | ⭐⭐ |
| 28 | `admin-dashboard-metrics` | KPIs: ingresos, pedidos procesados, productos más vendidos, gráficos recharts | orders-backend-core + payments-mercadopago-backend | ⭐⭐ |
| 29 | `error-handling-frontend` | Error boundary global, interceptor errores HTTP, toasts/notificaciones | frontend-core-setup | ⭐⭐ |
| 30 | `validation-and-sanitization` | Validación Pydantic, sanitización XSS, validación frontend | patterns-and-core-infrastructure | ⭐⭐ |

### **Fase 8: Seguridad y Optimización (7 changes)**
Protecciones y mejoras transversales.

| # | Change | Funcionalidad | Dependencias | Complejidad |
|---|--------|---------------|--------------|-------------|
| 31 | `rate-limiting-endpoints` | Rate limiting login 5/15min, registro 3/1h, pedidos 10/h | auth-backend-jwt | ⭐ |
| 32 | `testing-backend-core` | Tests unitarios y de integración para patrones base | patterns-and-core-infrastructure | ⭐⭐⭐ |
| 33 | `testing-auth-module` | Tests login, registro, refresh, logout, RBAC | auth-backend-jwt + rbac-authorization | ⭐⭐⭐ |
| 34 | `testing-orders-module` | Tests creación pedidos, FSM, transiciones, stock | orders-state-machine-backend | ⭐⭐⭐ |
| 35 | `testing-payments-module` | Tests integración MercadoPago, webhook, idempotencia | payments-mercadopago-backend | ⭐⭐ |
| 36 | `caching-and-performance` | Caching en TanStack Query, índices DB, query optimization | products-backend + orders-backend-core | ⭐⭐ |
| 37 | `deployment-and-docs` | Docker, docker-compose, CI/CD, documentación final API | Todos | ⭐⭐ |

---

## 📊 Dependencias Visuales

```
infrastructure-setup
├── database-design-migrations
│   ├── patterns-and-core-infrastructure
│   │   ├── auth-backend-jwt ────────────────────┐
│   │   │   ├── rbac-authorization ──────────┐   │
│   │   │   │   ├── categories-backend ──┐   │   │
│   │   │   │   │   └── products-backend ◄───┤   │
│   │   │   │   │       ├── product-catalog-frontend ──┐
│   │   │   │   │       │   └── cart-management-frontend ──┐
│   │   │   │   │       └── admin-stock-management      │
│   │   │   │   ├── ingredients-backend ─┤               │
│   │   │   │   ├── directions-backend ──┤               │
│   │   │   │   ├── admin-users-management-backend │     │
│   │   │   │   └── orders-backend-core ◄────────┤     │
│   │   │   │       ├── orders-state-machine-backend ◄──┤
│   │   │   │       │   ├── payments-mercadopago-backend ◄──────┐
│   │   │   │       │   │   ├── checkout-payment-frontend ◄───┤
│   │   │   │       │   │   └── admin-dashboard-metrics  │
│   │   │   │       │   └── admin-orders-management      │
│   │   │   │       └── orders-list-frontend             │
│   │   │   │
│   │   │   └── rate-limiting-endpoints
│   │   ├── validation-and-sanitization
│   │   └── testing-backend-core
│   │
│   ├── auth-frontend-login-register ◄────────────────────┐
│   ├── token-refresh-frontend ◄─────────────────────────┤
│   ├── frontend-navigation-layout ◄─────────────────────┤
│   └── error-handling-frontend                          │
│                                                         │
├── frontend-core-setup ◄─────────────────────────────────┘
│   └── zustand-stores-setup
│       ├── user-profile-frontend
│       ├── cart-management-frontend
│       │   └── checkout-payment-frontend
│       │       └── payment-status-frontend
│       └── auth-frontend-login-register
│           └── token-refresh-frontend
│               └── frontend-navigation-layout
│
├── testing-auth-module
├── testing-orders-module
├── testing-payments-module
├── caching-and-performance
└── deployment-and-docs
```

---

## ✅ Historias de Usuario por Change

### Autenticación
- **auth-backend-jwt**: US-001 (Registro), US-002 (Login), US-003 (Logout), US-004 (Refresh)
- **rbac-authorization**: US-005 (Roles), US-006 (Permisos)

### Catálogo
- **categories-backend**: US-007..010 (Gestión categorías)
- **ingredients-backend**: US-011..014 (Gestión ingredientes)
- **products-backend**: US-015..017, US-020..022 (CRUD productos)
- **product-catalog-frontend**: US-018, US-019, US-023 (Ver catálogo)

### Pedidos
- **orders-backend-core**: US-035..038 (Crear pedidos)
- **orders-state-machine-backend**: US-039..044 (Transiciones estado)
- **orders-list-frontend**: US-049..051 (Ver historial)

### Pagos
- **payments-mercadopago-backend**: US-045..048 (Pagos)
- **checkout-payment-frontend**: US-045 (Interfaz pago)

### Direcciones
- **directions-backend**: US-024..028 (Gestión direcciones)

### Admin
- **admin-users-management-backend**: US-052..055 (Usuarios)
- **admin-stock-management**: US-057..059, US-064 (Stock)
- **admin-orders-management**: US-060 (Gestión pedidos)
- **admin-dashboard-metrics**: US-065 (Métricas)

### Utilidad
- **validation-and-sanitization**: US-074 (Validaciones)
- **rate-limiting-endpoints**: US-073 (Rate limit)

---

## 🚀 Cómo Comenzar

### 1. Revisar esta propuesta
- Verificá que el orden tiene sentido
- Ajustá nombres, dependencias o alcance si necesitás
- Discutí cambios antes de comenzar

### 2. Proponer el primer change
```
/sdd-propose infrastructure-setup
```

### 3. Ciclo de cada change
```
1. Revisar proposal.md y design.md
2. Ejecutar: /sdd-apply infrastructure-setup
3. Verificar: /sdd-verify infrastructure-setup
4. Archivar: /sdd-archive infrastructure-setup
5. Pasar al siguiente change
```

---

## 📝 Reglas Críticas

1. **Nunca saltes cambios**: Si el change B depende de A, A debe estar archivado completamente
2. **Un change = un commit** (o varios commits atómicos). Nunca mezcles dos cambios
3. **Las specs son código**: Se versionan en git, se revisan en PRs
4. **Revisá antes de implementar**: Un error en design.md cuesta 0. El mismo error en código cuesta horas
5. **Mantené el DAG**: Si creés que falta algo, propone un nuevo change; no agregues tareas a uno existente
