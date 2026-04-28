# Food Store Frontend Setup

## Prerequisites

- Node.js 18+ and npm

## Installation

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file:
```bash
cp .env.example .env
# Edit .env with your configuration if needed
```

## Running the Development Server

```bash
npm run dev
```

The application will be available at http://localhost:5173

## Building for Production

```bash
npm run build
```

Output will be in the `dist/` directory.

## Preview Production Build

```bash
npm run preview
```

## Code Quality

Lint code:
```bash
npm run lint
```

Format code:
```bash
npm run format
```

## Project Structure (Feature-Sliced Design)

- `src/app/` - Application initialization (App.tsx, providers, global styles)
- `src/pages/` - Pages/routes of the application
- `src/widgets/` - Large UI components (composed from features and entities)
- `src/features/` - Business feature modules (features of the app)
- `src/entities/` - Domain entities (shared business entities)
- `src/shared/` - Shared utilities, configs, types
  - `config/` - Configuration (Axios, Query Client, etc)
  - `types/` - TypeScript types
  - `utils/` - Utility functions
  - `hooks/` - Reusable hooks
  - `ui/` - Generic UI components
  - `constants/` - Application constants

## Architecture

This project uses **Feature-Sliced Design (FSD)**, a methodology that organizes code into isolated, self-contained feature modules. Each layer has strict import rules:

- `app` → can import from all layers
- `pages` → can import from pages, widgets, features, entities, shared
- `widgets` → can import from widgets, features, entities, shared
- `features` → can import from features, entities, shared
- `entities` → can import from entities, shared
- `shared` → cannot import from other layers (lowest level)

This ensures a predictable, scalable architecture as the application grows.
