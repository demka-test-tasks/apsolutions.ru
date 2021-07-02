from sqlalchemy.orm import Session

import models
from elastic import MyElastic

my_elastic = MyElastic()


def search_post_by_text(db: Session, search_text: str):
    """Поиск по тексту документа и возврат первых 20 документов со всем полями, упорядоченные по дате создания"""
    # Поиск в elastic
    ids_list = my_elastic.search_by_text(search_text)
    # Получение полей СУБД с id, которые отдал нам elastic
    result = db.query(models.Post) \
        .filter(models.Post.id.in_(ids_list)) \
        .order_by(models.Post.created_date.desc()) \
        .all()
    return result


def delete_by_id(db: Session, id: int) -> bool:
    """Удаление поста по переданному id"""
    # Удаление из elastic
    delete_item = my_elastic.search_by_id(id)
    # Если в elastic есть такой id
    if delete_item is not None:
        # Удаляем по внутреннему id в elastic
        elastic_result = my_elastic.delete_by_id(delete_item[0]["_id"])
        # Если нам удалось удалить данные
        if elastic_result:
            # Удаляем по id СУБД в Postgre
            db_result = bool(db.query(models.Post).filter(models.Post.id == id).delete())
            db.commit()
            return db_result
        return elastic_result
    return False
