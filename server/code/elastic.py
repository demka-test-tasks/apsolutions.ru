from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self, connection_str: str = "http://localhost:9200"):
        self.connection = Elasticsearch(connection_str)

    def delete_index(self, id: int):
        self.connection
        """DELETE http://localhost:9200/posts/_doc/4yT__3kBMrhp05kiQYwf"""
        """DELETE /my-index-000001/_doc/1?routing=shard-1"""

    def search_index(self, text : str):
        pass
        """http://localhost:9200/posts/_search?q=привет"""
