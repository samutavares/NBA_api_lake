import duckdb

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"""
        CREATE TABLE silver_games AS
        
        select data_unest.id,
		    data_unest.date,
		    data_unest.season,
		    data_unest.status,
		    data_unest.period,
		    data_unest.home_team_score,
		    data_unest.visitor_team_score,
		    data_unest.home_team,
		    data_unest.visitor_team
        from (
                SELECT unnest(data) as data_unest
                FROM nba.main.games)
              """)
