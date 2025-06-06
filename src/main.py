from fastapi import FastAPI, Depends, APIRouter
from typing import Optional 
from fastapi.middleware.cors import CORSMiddleware
from routes import(login)

app = FastAPI(
    title="LEAVE MANAGEMENT SYSTEM",
    description = "ONLY FOR LMS"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(login.routes)