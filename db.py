from sqlmodel import SQLModel, create_engine

# DATABASE_URL tells SQLModel how to connect to MySQL:
# mysql+pymysql → use the PyMySQL driver
# root:@localhost → user root with no password on local server
# 3306 → default MySQL port
# weapons_db → the database name
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/weapons_db"

# create_engine creates the connection "engine" used by ORM operations.
# echo=True prints the actual SQL executed (useful for debugging).
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    # This command looks at all SQLModel classes with table=True
    # and automatically creates tables in the database if they don't exist.
    SQLModel.metadata.create_all(engine)
