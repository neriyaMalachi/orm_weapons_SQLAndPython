from fastapi import FastAPI
from db import create_db_and_tables
from api.routes_customers import router as customers_router
from api.routes_orders import router as orders_router

app = FastAPI()

# connect to sql server
create_db_and_tables()

# Routers (new for students hermon :) )
app.include_router(customers_router)
app.include_router(orders_router)

# Root
@app.get("/")
def healthcheck():
    return {"status": "server run ok"}
