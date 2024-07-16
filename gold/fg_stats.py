import duckdb

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"""
        CREATE TABLE gold_fg_ratio AS
        
        SELECT t.player_id ,
              p.first_name , 
              p.last_name, 
              SUM(fgm) AS total_fgm, SUM(fga) AS total_fga, CAST(SUM(fgm) AS FLOAT) / SUM(fga) AS fgm_fga_ratio
        FROM main.silver_stats t
        JOIN main.silver_players p ON t.player_id = p.id
        GROUP BY t.player_id,p.first_name , p.last_name
        ORDER BY fgm_fga_ratio DESC
              """)
