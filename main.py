from db import create_db_and_tables, engine
from sqlmodel import Session, select
from models import Weapon

# Create all tables based on the SQLModel classes (only if they don't exist)
create_db_and_tables()

# --- INSERT A NEW ROW (Weapon) INTO THE DATABASE ---
with Session(engine) as session:              # Open a session (a connection context) to interact with the DB
    weapon = Weapon(                           # Create a new Weapon object (represents a row)
        name="AK-47",
        type="firearm",
        price=3500
    )
    session.add(weapon)                        # Add the new object to the session (prepare INSERT)
    session.commit()                           # Commit = execute the INSERT in the actual database

# --- SELECT ALL WEAPONS FROM THE DATABASE ---
with Session(engine) as session:              # Open a new session for reading data
    result = session.exec(select(Weapon)).all()  # Build a SELECT query → run it → return all rows as objects
    print(result)                               # Print the list of Weapon objects retrieved from the DB
