"""Orders endpoints"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.get("/")
async def list_orders():
    """List all orders (stub)"""
    return {"message": "Orders endpoint - not yet implemented"}


@router.get("/{order_id}")
async def get_order(order_id: int):
    """Get order by ID (stub)"""
    return {"order_id": order_id, "message": "Get order endpoint - not yet implemented"}


@router.post("/")
async def create_order(order_data: dict):
    """Create a new order (stub)"""
    return {"message": "Create order endpoint - not yet implemented"}


@router.put("/{order_id}")
async def update_order(order_id: int, order_data: dict):
    """Update order (stub)"""
    return {"order_id": order_id, "message": "Update order endpoint - not yet implemented"}


@router.delete("/{order_id}")
async def delete_order(order_id: int):
    """Delete order (stub)"""
    return {"order_id": order_id, "message": "Delete order endpoint - not yet implemented"}
