from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from config import Settings as settings
from urllib.parse import quote_plus

# Connection
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{quote_plus(settings.POSTGRES_PASSWORD)}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
print(DATABASE_URL,'++++++++++++++')

engine = create_engine(DATABASE_URL)

Base = declarative_base(metadata = MetaData(schema='public') )
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()