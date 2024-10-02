from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.config import settings

engine = create_engine(settings.DATABASE_URL)
SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()
