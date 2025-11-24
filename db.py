from sqlmodel import SQLModel, create_engine, Session

engine = create_engine( "mysql+pymysql://root:@localhost:3306/customerAndOrdersDATA", echo=False, pool_pre_ping=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
