import os
from typing import List, Union

import elasticsearch
from elasticsearch import Elasticsearch


class MyElastic:
    def __init__(self, index: str = "posts"):
        connection_str = os.getenv("SERVER_ELASTIC_CONNECTION", None)
        self.__connection = Elasticsearch(connection_str)
        self.__index = index

    def search_by_id(self, id: int) -> Union[list, None]:
        """Поиск элемента по идентификатору СУБД"""
        result = self.__connection.search(index=self.__index, body={
            "size": 1,
            "query": {
                "match": {
                    'id': id
                }
            }
        })["hits"]["hits"]

        # Если ничего не нашли
        if len(result) == 0:
            return None
        # Если результат есть
        return result

    def delete_by_id(self, id: int) -> bool:
        """
        Удаление элементов индекса по внутреннему _id
        """
        try:
            self.__connection.delete(index=self.__index, doc_type="record", id=id)
            return True
        except elasticsearch.exceptions.NotFoundError:
            return False

    def search_by_text(self, text: str) -> List[dict]:
        """
        Поиск постов по тексту, возвращает список элементов БД
        """
        result = self.__connection.search(index=self.__index, body={
            "size": 20,
            "query": {
                "match": {
                    'text': text
                }
            }
        })
        result_ids = [{"id_": item["_id"], "id": item["_source"]["id"]} for item in result["hits"]["hits"]]
        return result_ids
