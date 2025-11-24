from typing import List, Optional
from sqlmodel import Session, select
from models import Customer, Order

# -------- Customers SQL functions --------

def create_customer_sql(session: Session, *, name: str, country: str = "IL") -> Customer:
    obj = Customer(name=name, country=country)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

def list_customers_sql(session: Session, *, country: Optional[str] = None,
                       skip: int = 0, limit: int = 50) -> List[Customer]:
    stmt = select(Customer)
    if country:
        stmt = stmt.where(Customer.country == country)
    stmt = stmt.order_by(Customer.id).offset(skip).limit(limit)
    return session.exec(stmt).all()

def get_customer_sql(session: Session, customer_id: int) -> Optional[Customer]:
    return session.get(Customer, customer_id)

def update_customer_sql(session: Session, customer_id: int, *,
                        name: str, country: str) -> Optional[Customer]:
    obj = session.get(Customer, customer_id)
    if not obj:
        return None
    obj.name = name
    obj.country = country
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

def delete_customer_sql(session: Session, customer_id: int) -> bool:
    obj = session.get(Customer, customer_id)
    if not obj:
        return False
    session.delete(obj)
    session.commit()
    return True

# Orders SQL functions \

def create_order_sql(session: Session, *, customer_id: int, total: float) -> Optional[Order]:
    if session.get(Customer, customer_id) is None:
        return None  # הלקוח לא קיים
    obj = Order(customer_id=customer_id, total=total)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

def list_orders_sql(session: Session, *, skip: int = 0, limit: int = 50) -> List[Order]:
    stmt = select(Order).order_by(Order.created_at.desc()).offset(skip).limit(limit)
    return session.exec(stmt).all()

def get_order_sql(session: Session, order_id: int) -> Optional[Order]:
    return session.get(Order, order_id)

# Composite: Customer with Orders (ללא Relationships)

def get_customer_with_orders_sql(session: Session, customer_id: int) -> Optional[tuple[Customer, List[Order]]]:
    c = session.get(Customer, customer_id)
    if not c:
        return None
    orders = session.exec(
        select(Order).where(Order.customer_id == customer_id).order_by(Order.created_at.desc())
    ).all()
    return (c, orders)
