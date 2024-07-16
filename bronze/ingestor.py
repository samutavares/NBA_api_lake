import polars as pl
import duckdb

import os
from datetime import datetime, timedelta

endpoint='stats'
folder_path = f'C:\\Users\\Samuel\\Desktop\\NBA_API\\raw\\data\\{endpoint}\\'

today = datetime.now().strftime('%Y%m%d')
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
print(yesterday)
json_files = [f for f in os.listdir(folder_path) if (f.startswith(today) or f.startswith(yesterday)) and f.endswith('.json')]
print(json_files)

dataframes = []

for json_file in json_files:
    file_path = os.path.join(folder_path, json_file)
    df = pl.read_json(file_path)
    try:
        df = df.drop(["meta"])
    except:
        print("Nao existe meta")
    dataframes.append(df)

combined_df = pl.concat(dataframes)

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.execute(f"""
        CREATE TABLE IF NOT EXISTS '{endpoint}' AS SELECT * FROM combined_df;
    """)

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"SELECT * FROM {endpoint}").show()

# result = con.execute(f"SELECT * FROM temp_{endpoint}").fetchdf()

# print(result)

# con.execute(f"CREATE TABLE persistent_{endpoint} AS SELECT * FROM temp_{endpoint}")

# con.close()