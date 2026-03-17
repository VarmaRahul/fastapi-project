from fastapi import APIRouter
from app.models.schemas import OrderBase

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def list_orders():
    return [{"id": 1, "item": "Cloud Architecture Book", "status": "shipped"}]

@router.post("/")
def create_order(order: OrderBase):
    return {"message": "Order created", "details": order}