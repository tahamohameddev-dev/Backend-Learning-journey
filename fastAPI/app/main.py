from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from typing import Optional, List 
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, get_db
from .routers import post, user, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
        user='postgres', password='taha116741', cursor_factory=RealDictCursor)   
        cursor = conn.cursor()
        print("Database connection was successfully!")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(3)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello world"}

