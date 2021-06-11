"""
Конвертер данных с .csv в СУБД postgres
"""
import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('posts.csv')
print(df)

df.columns = [c.lower() for c in df.columns]
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/test_task')
df.to_sql("posts", engine)
print("ok")