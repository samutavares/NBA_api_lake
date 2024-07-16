import duckdb

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"""
        CREATE TABLE silver_teams AS
        
        SELECT
            teams.id,
            teams.conference,
            teams.division,
            teams.city,
            teams."name",
            teams.full_name,
            teams.abbreviation
        FROM (
            SELECT unnest(data) AS teams
                FROM teams)
              """)