from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlmodel import Session

from db import get_session
from models import Order
from sql_functions import create_order_sql, list_orders_sql, get_order_sql

router = APIRouter(prefix="/orders", tags=["orders"])

class OrderIn(BaseModel):
    customer_id: int
    total: float

@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(data: OrderIn, session: Session = Depends(get_session)):
    obj = create_order_sql(session, customer_id=data.customer_id, total=data.total)
    if obj is None:
        raise HTTPException(status_code=400, detail="customer_id does not exist")
    return obj

@router.get("/", response_model=List[Order])
def list_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    session: Session = Depends(get_session),
):
    return list_orders_sql(session, skip=skip, limit=limit)

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, session: Session = Depends(get_session)):
    obj = get_order_sql(session, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Order not found")
    return obj
