# 🏀 NBA Analytics Dashboard

🚀 **LIVE DASHBOARD (Top Priority for Evaluation)**  
👉 **https://nba-analytics-dashboard.streamlit.app/**

> An interactive NBA analytics dashboard built using **Python and Streamlit** that provides season-wise, team-wise, and player-wise insights through dynamic visualizations.

---

## 📌 Project Objective

The goal of this project is to analyze historical NBA data and present meaningful insights through an **interactive analytics dashboard**.  
The dashboard enables users to explore:
- Scoring and performance trends across seasons
- Team rankings and win–loss patterns
- Player performance and consistency
- Game-wise performance evolution

This project is designed to support **data-driven decision making** and **sports analytics exploration**.

---

## 🛠️ Technology Stack

| Component | Technology |
|---------|------------|
| Programming Language | Python |
| Dashboard Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly |
| Deployment | Streamlit Community Cloud |

---

## 🚀 Live Application Access

The dashboard is already deployed and can be accessed directly:

👉 **https://nba-analytics-dashboard.streamlit.app/**

> Evaluators can review the project using the live link without setting up any local environment.

---

## 📊 Dashboard Features & Analytics Coverage

### 🔹 1. Season-wise Scoring Trends
- Average **home vs away points per game** across seasons
- Visualization of league-wide scoring evolution
- Helps identify offensive trends over time

### 🔹 2. Game-wise Performance Analysis
- Game-by-game scoring trends within a selected season
- Comparison of home and away team performances
- Useful for identifying momentum and scoring volatility

### 🔹 3. Team Analysis & Rankings
- Aggregated win–loss records across seasons
- Team ranking based on **win percentage**
- Identification of long-term dominant teams

### 🔹 4. Player Performance Insights
- Average **points, rebounds, and assists**
- Bubble chart visualization to highlight standout players
- Enables comparison of player consistency and impact

### 🔹 5. Interactive Filters
- **Season filter** for temporal analysis
- **Team filter** for focused team performance
- **Player filter** for individual player analysis
- All visualizations update dynamically based on selections

### 🔹 6. Insight Narration
- Automatically generated analytical summaries
- Provides contextual understanding of the visualizations

---

## 📁 Project Directory Structure

nba-analytics-dashboard/
│── app.py # Main Streamlit application
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── games.csv # Game-level results
│── games_details.csv # Player box-score details
│── players.csv # Player metadata
│── teams.csv # Team metadata
│── ranking.csv # Team rankings & win–loss records



---

## ▶️ Running the Project Locally (Optional)

> This step is optional since the app is already live.

### Prerequisites
- Python 3.9+
- pip installed

### Steps
1. Extract the ZIP submission
2. Open terminal in the project directory
3. Install required packages:
   ```bash
   pip install -r requirements.txt

4. streamlit run app.py
