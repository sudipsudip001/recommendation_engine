from db.session import engine
from db.models.user import User
from sqlmodel import SQLModel

def init_db():
    print("📦 Creating database tables...")
    SQLModel.metadata.create_all(engine)

