"""Users endpoints"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/")
async def list_users():
    """List all users (stub)"""
    return {"message": "Users endpoint - not yet implemented"}


@router.get("/{user_id}")
async def get_user(user_id: int):
    """Get user by ID (stub)"""
    return {"user_id": user_id, "message": "Get user endpoint - not yet implemented"}


@router.post("/")
async def create_user(user_data: dict):
    """Create a new user (stub)"""
    return {"message": "Create user endpoint - not yet implemented"}


@router.put("/{user_id}")
async def update_user(user_id: int, user_data: dict):
    """Update user (stub)"""
    return {"user_id": user_id, "message": "Update user endpoint - not yet implemented"}


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Delete user (stub)"""
    return {"user_id": user_id, "message": "Delete user endpoint - not yet implemented"}
