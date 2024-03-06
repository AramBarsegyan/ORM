from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from comp.base import Base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/arutdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Инициализация базы данных.
    """
    Base.metadata.create_all(bind=engine)