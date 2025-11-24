from __future__ import annotations
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    country: str = Field(default="IL", index=True)

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id", index=True)
    total: float = Field(gt=0)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
