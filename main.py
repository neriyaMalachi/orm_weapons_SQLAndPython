from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from db import create_db_and_tables, get_session
from models import Customer

app = FastAPI()
create_db_and_tables()


#      GET ALL
@app.get("/customers")
def get_customers(session: Session = Depends(get_session)):
    customers = session.exec(select(Customer)).all()
    return customers

#   GET BY ID
@app.get("/customers/{customer_id}")
def get_customer_by_id(customer_id: int, session: Session = Depends(get_session)):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.get("/")
def health():
    return {"status": "ok"}
