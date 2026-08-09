from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from . import models, schemas
from sqlalchemy.orm import Session
from .database import engine, get_db

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


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/posts")
def get_post(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM post""")
    #post = cursor.fetchall()
    posts = db.query(models.post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def createpost(post: schemas.PostCreate, db: Session = Depends(get_db)):
    #cursor.execute("""INSERT INTO post(title, content, published) VALUES(%s, %s, %s) RETURNING *""",
    #(post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    new_post = models.post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM post WHERE id = %s """, (str(id),))
    #post = cursor.fetchone()
    post = db.query(models.post).filter(models.post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post detaile": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT )
def delete_post(id: int, db: Session = Depends(get_db)):
    
    #cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""", (str(id),))
    #delete_post = cursor.fetchone()
    #conn.commit()
    post = db.query(models.post).filter(models.post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} dose not exist")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, update_post: schemas.PostCreate, db: Session = Depends(get_db)):

    #cursor.execute("""UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #(post.title, post.content, post.published, str(id),))

    #update_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.post).filter(models.post.id == id)
    post = post_query.first()
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} dose not exist")

    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    
    return {"data": post_query.first()}


