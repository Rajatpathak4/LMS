from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from Database.database import get_db
from modules.login import crud, schema


routes = APIRouter(tags=["Login"])


@routes.post('/login')
def login(db:Session= Depends(get_db)):
    try:
        response = crud.login(db)
        return response
    except Exception as err:
        print(err)