import models
import schemas
from sqlalchemy.orm import Session
from sqlalchemy import update


# TODO пока так, попозже пойму, что такое эластик и как его сюда добавить
def search_post_by_text(db: Session, search_text: str):
    """Поиск по тексту документа и возврат первых 20 документов со всем полями, упорядоченные по дате создания"""
    #Поиск в elastic


    result = db.query(models.Post) \
        .filter(models.Post.text.contains(search_text)) \
        .order_by(models.Post.created_date.desc()) \
        .limit(20) \
        .all()
    return result


def delete_by_id(db: Session, id: int) -> bool:
    """Удаление поста по переданному id"""
    #Удаление из elastic


    #Удаелние из СУБД
    result = db.query(models.Post).filter(models.Post.id == id).delete()
    db.commit()
    return bool(result)
