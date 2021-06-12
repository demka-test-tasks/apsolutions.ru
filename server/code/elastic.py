from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self, connection_str: str = "http://localhost:9200"):
        self.connection = Elasticsearch(connection_str)

    def delete_index(self, id : int):
        self.connection

    def search_index(self, text : str):
        pass
        """http://localhost:9200/posts/_search?q=привет"""
