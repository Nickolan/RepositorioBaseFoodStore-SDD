"""Products endpoints"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def list_products():
    """List all products (stub)"""
    return {"message": "Products endpoint - not yet implemented"}


@router.get("/{product_id}")
async def get_product(product_id: int):
    """Get product by ID (stub)"""
    return {"product_id": product_id, "message": "Get product endpoint - not yet implemented"}


@router.post("/")
async def create_product(product_data: dict):
    """Create a new product (stub)"""
    return {"message": "Create product endpoint - not yet implemented"}


@router.put("/{product_id}")
async def update_product(product_id: int, product_data: dict):
    """Update product (stub)"""
    return {"product_id": product_id, "message": "Update product endpoint - not yet implemented"}


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    """Delete product (stub)"""
    return {"product_id": product_id, "message": "Delete product endpoint - not yet implemented"}
