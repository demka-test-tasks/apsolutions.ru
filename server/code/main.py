# coding=utf-8
from datetime import datetime
import shutil
from typing import List, Union

import os
import util
import crud
import models
import schemas
import uvicorn
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session

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
def search_post(db: Session = Depends(get_db)):
    """сервис должен принимать на вход произвольный текстовый запрос, искать по тексту документа в индексе и возвращать первые 20 документов со всем полями БД, упорядоченные по дате создания;"""
    pass


@app.delete("/posts/delete")
def remove_post(db: Session = Depends(get_db)):
    """удалять документ из БД и индекса по полю  `id`."""
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=False, use_colors=True)
