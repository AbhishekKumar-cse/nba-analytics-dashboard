import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="NBA Analytics Dashboard",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA (CLOUD-SAFE)
# --------------------------------------------------
@st.cache_data
def load_data():
    games = pd.read_csv("games.csv")
    game_details = pd.read_csv("games_details.csv", low_memory=False)
    players = pd.read_csv("players.csv")
    teams = pd.read_csv("teams.csv")
    ranking = pd.read_csv("ranking.csv")
    return games, game_details, players, teams, ranking

games, game_details, players, teams, ranking = load_data()

# --------------------------------------------------
# CONSTANTS (FROM YOUR CSV)
# --------------------------------------------------
TEAM_COL = "NICKNAME"   # ✅ confirmed column

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🏀 NBA Analytics Dashboard")
st.caption("Interactive NBA Analytics | Python • Streamlit • Plotly")

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("Filters")

season = st.sidebar.selectbox(
    "Season",
    sorted(games["SEASON"].dropna().unique())
)

team_name = st.sidebar.selectbox(
    "Team",
    ["All"] + sorted(teams[TEAM_COL].unique())
)

player_name = st.sidebar.selectbox(
    "Player",
    ["All"] + sorted(players["PLAYER_NAME"].unique())
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------
filtered_games = games[games["SEASON"] == season]

if team_name != "All":
    team_id = teams.loc[
        teams[TEAM_COL] == team_name, "TEAM_ID"
    ].values[0]

    filtered_games = filtered_games[
        (filtered_games["HOME_TEAM_ID"] == team_id) |
        (filtered_games["VISITOR_TEAM_ID"] == team_id)
    ]

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Games", len(filtered_games))
col2.metric("Avg Home Points", round(filtered_games["PTS_home"].mean(), 1))
col3.metric("Avg Away Points", round(filtered_games["PTS_away"].mean(), 1))

# --------------------------------------------------
# SEASON-WISE SCORING TRENDS
# --------------------------------------------------
st.subheader("📈 Season-wise Scoring Trends")

season_trend = (
    games.groupby("SEASON")[["PTS_home", "PTS_away"]]
    .mean()
    .reset_index()
)

fig1 = px.line(
    season_trend,
    x="SEASON",
    y=["PTS_home", "PTS_away"],
    labels={"value": "Average Points", "variable": "Game Type"},
    markers=True
)
st.plotly_chart(fig1, use_container_width=True)

# --------------------------------------------------
# TEAM RANKINGS & WIN–LOSS
# --------------------------------------------------
st.subheader("🏆 Team Rankings (Win–Loss Patterns)")

team_rank = ranking.groupby("TEAM_ID")[["W", "L"]].sum().reset_index()
team_rank["WIN_PCT"] = team_rank["W"] / (team_rank["W"] + team_rank["L"])
team_rank = team_rank.merge(
    teams[["TEAM_ID", TEAM_COL]],
    on="TEAM_ID"
)

fig2 = px.bar(
    team_rank.sort_values("WIN_PCT", ascending=False).head(10),
    x=TEAM_COL,
    y="WIN_PCT",
    title="Top 10 Teams by Win Percentage"
)
st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# PLAYER INSIGHTS
# --------------------------------------------------
st.subheader("👤 Player Performance Insights")

player_stats = (
    game_details
    .groupby("PLAYER_ID")[["PTS", "REB", "AST"]]
    .mean()
    .reset_index()
    .merge(players[["PLAYER_ID", "PLAYER_NAME"]], on="PLAYER_ID")
)

if player_name != "All":
    player_stats = player_stats[player_stats["PLAYER_NAME"] == player_name]

fig3 = px.scatter(
    player_stats.sort_values("PTS", ascending=False).head(20),
    x="PTS",
    y="REB",
    size="AST",
    color="PLAYER_NAME",
    title="Top Players: Points vs Rebounds (Bubble = Assists)"
)
st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# GAME-WISE PERFORMANCE TREND
# --------------------------------------------------
st.subheader("📅 Game-wise Scoring Trend")

game_trend = filtered_games.sort_values("GAME_DATE_EST")

fig4 = px.line(
    game_trend,
    x="GAME_DATE_EST",
    y=["PTS_home", "PTS_away"],
    title="Game-wise Scoring Trend"
)
st.plotly_chart(fig4, use_container_width=True)

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------
st.subheader("🧠 Key Insights")

st.info(
    f"""
    🔹 Season **{season}** shows a strong home-court advantage  
    🔹 Team rankings reveal long-term performance dominance  
    🔹 Player insights highlight consistent top performers  
    🔹 Game-wise trends reflect evolving offensive strategies  
    """
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("NBA Analytics Dashboard | Streamlit Community Cloud")
