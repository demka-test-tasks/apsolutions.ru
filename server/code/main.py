# coding=utf-8

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    version="1.0",
    title="Test task",
    description="My test task",
)


# Коннект с СУБД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/posts/search")
def search_post(text: str, db: Session = Depends(get_db)):
    """Поиск постов по тексту"""
    results_list = crud.search_post_by_text(db=db, search_text=text)
    return {"result": results_list}


@app.delete("/posts/delete")
def remove_post(remove_item: schemas.PostRemoveItem, db: Session = Depends(get_db)):
    """удалять документ из БД и индекса по полю id."""
    result = crud.delete_by_id(db=db, id=remove_item.id)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=False, use_colors=True)
