from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from Database.database import get_db
from modules.login import crud, schema


routes = APIRouter(tags=["Login"])


@routes.post('/login')
def login(request: schema.LoginUser, db:Session= Depends(get_db)):
    try:
        response = crud.login(request,db)
        return response
    except Exception as err:
        return line_error_details(err)
        
@routes.post('/authenticate_user')
def authenticate_user(request: schema.LoginUser, db:Session= Depends(get_db)):
    try:
        response = crud.authenticate_user(request,db)
        return response
    except Exception as err:
        return line_error_details(err)