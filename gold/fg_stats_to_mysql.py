import duckdb
import polars as pl
from sqlalchemy import create_engine
import pandas as pd

con_duckdb = duckdb.connect(database='nba.db', read_only=False)
query = "SELECT * FROM gold_fg_ratio"
df = con_duckdb.execute(query).fetchdf()  # Fetch the data as a Polars DataFrame
con_duckdb.close()


mysql_connection_string = 'mysql+mysqlconnector://root:root@localhost:3306/gold'
engine = create_engine(mysql_connection_string)

df.to_sql('fg_ratio', con=engine, if_exists='replace', index=False)

engine.dispose()
