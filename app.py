def process_order(order_id: str, amount: float) -> dict:
    if amount <= 0:
        raise ValueError("Invalid amount")
    return {"order_id": order_id, "amount": amount, "status": "CONFIRMED"}
