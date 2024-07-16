import duckdb

with duckdb.connect(database="nba.db", read_only=False) as con:
    con.query(f"""
        CREATE TABLE silver_stats AS
        
        SELECT
            data_unnest.id,
            data_unnest.min,
            data_unnest.fgm,
            data_unnest.fga,
            data_unnest.fg_pct,
            data_unnest.fg3m,
            data_unnest.fg3a,
            data_unnest.fg3_pct,
            data_unnest.ftm,
            data_unnest.fta,
            data_unnest.ft_pct,
            data_unnest.oreb,
            data_unnest.dreb,
            data_unnest.reb,
            data_unnest.ast,
            data_unnest.stl,
            data_unnest.blk,
            data_unnest.turnover,
            data_unnest.pf,
            data_unnest.pts,
            data_unnest.player.id AS player_id,
            data_unnest.player.first_name,
            data_unnest.player.last_name,
            data_unnest.player."position",
            data_unnest.player.height,
            data_unnest.player.weight,
            data_unnest.player.jersey_number,
            data_unnest.player.college,
            data_unnest.player.country,
            data_unnest.player.draft_year,
            data_unnest.player.draft_round,
            data_unnest.player.draft_number,
            data_unnest.player.team_id,
            data_unnest.team.id AS team_id,
            data_unnest.team.conference,
            data_unnest.team.division,
            data_unnest.team.city,
            data_unnest.team."name",
            data_unnest.team.full_name,
            data_unnest.team.abbreviation
    FROM (
    SELECT unnest(data) as data_unnest
    FROM stats
    )
              """)