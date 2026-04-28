.PHONY: help setup dev install install-backend install-frontend format lint clean logs

help:
	@echo "Food Store - Make Commands"
	@echo ""
	@echo "setup           - Install all dependencies (backend + frontend)"
	@echo "dev             - Start both backend and frontend servers"
	@echo "install         - Install all dependencies"
	@echo "install-backend - Install backend dependencies only"
	@echo "install-frontend- Install frontend dependencies only"
	@echo "format          - Format code (backend + frontend)"
	@echo "lint            - Run linters (backend + frontend)"
	@echo "clean           - Clean all build artifacts and caches"
	@echo "help            - Show this help message"

setup: install
	@echo "✅ Setup complete! Run 'make dev' to start the servers."

dev:
	@echo "🚀 Starting Food Store (backend + frontend)..."
	@echo ""
	@echo "Backend:  http://localhost:8000"
	@echo "Frontend: http://localhost:5173"
	@echo "Docs:     http://localhost:8000/docs"
	@echo ""
	@echo "Press Ctrl+C to stop both servers."
	@echo ""
	@(cd backend && python main.py) & \
	(cd frontend && npm run dev) & \
	wait

install: install-backend install-frontend

install-backend:
	@echo "📦 Installing backend dependencies..."
	@cd backend && pip install -r requirements.txt
	@echo "✅ Backend dependencies installed"

install-frontend:
	@echo "📦 Installing frontend dependencies..."
	@cd frontend && npm install
	@echo "✅ Frontend dependencies installed"

format:
	@echo "🎨 Formatting code..."
	@cd frontend && npm run format
	@echo "✅ Code formatted"

lint:
	@echo "🔍 Running linters..."
	@cd frontend && npm run lint
	@echo "✅ Linting complete"

clean:
	@echo "🗑️  Cleaning build artifacts..."
	@rm -rf backend/__pycache__ backend/.pytest_cache backend/.coverage
	@rm -rf frontend/node_modules frontend/dist
	@rm -rf .DS_Store
	@echo "✅ Clean complete"

.PHONY: help setup dev install install-backend install-frontend format lint clean
