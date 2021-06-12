"""
Конвертер данных с .csv в СУБД postgres
"""

import pandas as pd
from sqlalchemy import create_engine
from elasticsearch import helpers, Elasticsearch
from espandas import Espandas
import csv

INDEX = "posts"
TYPE = "record"

def rec_to_actions(df):
    import json
    for record in df.to_dict(orient="records"):
        yield ('{ "index" : { "_index" : "%s", "_type" : "%s" }}' % (INDEX, TYPE))
        yield (json.dumps(record, default=int))



def to_postgre(file_name : str):
    df = pd.read_csv(file_name)
    print(df)
    df.columns = [c.lower() for c in df.columns]
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/test_task')
    df.to_sql("posts", engine)
    print("Запись в БД есть")

def to_elastic(file_name : str):
    #df = pd.read_csv(file_name)
    new_filename = "./posts_short.csv"
    df = pd.read_csv(file_name, usecols=[0])

    e = Elasticsearch()  # no args, connect to localhost:9200
    if not e.indices.exists(INDEX):
        raise RuntimeError('index does not exists, use `curl -X PUT "localhost:9200/%s"` and try again' % INDEX)

    r = e.bulk(rec_to_actions(df))  # return a dict

    print(not r["errors"])

def main():
    file_name = "./posts.csv"
    #to_postgre(file_name)
    to_elastic(file_name)

if __name__ == "__main__":
    main()