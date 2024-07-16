import duckdb

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"""
        CREATE TABLE silver_players AS
        
                SELECT 
                data_unest.id,
                data_unest.first_name,
                data_unest.last_name,
                data_unest."position",
                data_unest.height,
                data_unest.weight,
                data_unest.jersey_number,
                data_unest.college,
                data_unest.country,
                data_unest.draft_year,
                data_unest.draft_round,
                data_unest.draft_number,
                data_unest.team
        from (SELECT unnest(data) as data_unest
                        FROM nba.main.players)
              """)