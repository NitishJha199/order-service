from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI(title="Order Service", version="1.2.0")

class OrderItem(BaseModel):
    item_id: str
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    customer_id: str
    items: list[OrderItem]

orders_db = {}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "order-service", "timestamp": datetime.datetime.utcnow()}

@app.post("/orders")
def create_order(order: OrderCreate):
    total = sum(i.quantity * i.unit_price for i in order.items)
    order_id = f"ORD-{len(orders_db) + 1001}"
    orders_db[order_id] = {
        "customer_id": order.customer_id,
        "total_amount": round(total, 2),
        "status": "CONFIRMED",
        "created_at": str(datetime.datetime.utcnow())
    }
    return {"order_id": order_id, "details": orders_db[order_id]}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]
