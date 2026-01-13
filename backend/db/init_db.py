from db.base import SQLModel
from db.session import engine

def init_db():
    SQLModel.metadata.create_all(bind=engine)
    print("📦 Tables created:", SQLModel.metadata.tables.keys())

