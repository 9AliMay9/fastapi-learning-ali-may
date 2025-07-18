from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create engine of database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base
Base = declarative_base()

# Create Session type
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Get session of database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

