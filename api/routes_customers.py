from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlmodel import Session
from db import get_session
from models import Customer
from sql_functions import (
    create_customer_sql, list_customers_sql, get_customer_sql,
    update_customer_sql, delete_customer_sql, get_customer_with_orders_sql
)

router = APIRouter(prefix="/customers")

# מודלי קלט קטנים ל-HTTP (לא שכבת DB)
class CustomerIn(BaseModel):
    name: str
    country: str = "IL"

class OrderShort(BaseModel):
    id: int
    total: float
    created_at: str

class CustomerWithOrders(BaseModel):
    id: int
    name: str
    country: str
    orders: List[OrderShort]

@router.post("/", response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(data: CustomerIn, session: Session = Depends(get_session)):
    return create_customer_sql(session, name=data.name, country=data.country)

@router.get("/", response_model=List[Customer])
def list_customers(
    country: Optional[str] = Query(default=None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    session: Session = Depends(get_session),
):
    return list_customers_sql(session, country=country, skip=skip, limit=limit)

@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: int, session: Session = Depends(get_session)):
    obj = get_customer_sql(session, customer_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    return obj

@router.patch("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, data: CustomerIn, session: Session = Depends(get_session)):
    obj = update_customer_sql(session, customer_id, name=data.name, country=data.country)
    if not obj:
        raise HTTPException(status_code=404, detail="Customer not found")
    return obj

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, session: Session = Depends(get_session)):
    ok = delete_customer_sql(session, customer_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Customer not found")
    return None

@router.get("/{customer_id}/with-orders", response_model=CustomerWithOrders)
def get_customer_with_orders(customer_id: int, session: Session = Depends(get_session)):
    data = get_customer_with_orders_sql(session, customer_id)
    if not data:
        raise HTTPException(status_code=404, detail="Customer not found")
    c, orders = data
    return CustomerWithOrders(
        id=c.id, name=c.name, country=c.country,
        orders=[OrderShort(id=o.id, total=o.total, created_at=o.created_at.isoformat()) for o in orders]
    )
