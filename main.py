from db import create_db_and_tables, engine
from sqlmodel import Session, select
from models import Weapon

create_db_and_tables()

with Session(engine) as session:
    weapon = Weapon(name="AK-47", type="firearm", price=3500)
    session.add(weapon)
    session.commit()

with Session(engine) as session:
    result = session.exec(select(Weapon)).all()
    print(result)
