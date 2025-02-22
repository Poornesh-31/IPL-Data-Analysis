import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import os

def load_data(matches_path, deliveries_path):
    """Load datasets and return DataFrames."""
    if os.path.exists(matches_path) and os.path.exists(deliveries_path):
        matches = pd.read_csv(matches_path)
        deliveries = pd.read_csv(deliveries_path)
        return matches, deliveries
    else:
        raise FileNotFoundError("One or both datasets not found.")

def preprocess_data(matches, deliveries):
    """Clean and preprocess the data."""
    matches.dropna(inplace=True)
    deliveries.fillna(0, inplace=True)
    matches["date"] = pd.to_datetime(matches["date"])

def plot_match_outcome(matches):
    """Plot the total wins by each team."""
    team_wins = matches["winner"].value_counts()
    plt.figure(figsize=(10,5))
    sns.barplot(x=team_wins.index, y=team_wins.values, palette="viridis")
    plt.xticks(rotation=90)
    plt.title("Total Wins by Each Team")
    plt.show()

def plot_venue_performance(matches):
    """Plot top 10 venues with the most matches."""
    venue_counts = matches["venue"].value_counts().head(10)
    sns.barplot(x=venue_counts.values, y=venue_counts.index, palette="coolwarm")
    plt.title("Top 10 Venues with Most Matches")
    plt.show()

def plot_player_performance(deliveries):
    """Plot top 10 batsmen and bowlers in IPL."""
    top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(10)
    sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette="magma")
    plt.title("Top 10 Run Scorers in IPL")
    plt.show()

    top_bowlers = deliveries[deliveries["dismissal_kind"].notnull()].groupby("bowler")["dismissal_kind"].count().sort_values(ascending=False).head(10)
    sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette="plasma")
    plt.title("Top 10 Wicket-Takers in IPL")
    plt.show()

def plot_run_rate(deliveries):
    """Plot average run rate per team."""
    team_run_rate = deliveries.groupby("batting_team")["total_runs"].sum() / deliveries.groupby("batting_team")["over"].nunique()
    team_run_rate.sort_values(ascending=False).plot(kind="bar", figsize=(10,5), color="teal")
    plt.title("Average Run Rate per Team")
    plt.show()

def plot_team_comparison(matches):
    """Plot win percentage of teams."""
    win_percentage = (matches["winner"].value_counts() / matches["winner"].count()) * 100
    sns.barplot(x=win_percentage.index, y=win_percentage.values, palette="coolwarm")
    plt.xticks(rotation=90)
    plt.title("Win Percentage of Teams")
    plt.show()

def plot_batting_partnerships(deliveries):
    """Plot top 10 batting partnerships in IPL."""
    batting_pairs = deliveries.groupby(["batsman", "non_striker"])['total_runs'].sum().sort_values(ascending=False).head(10)
    batting_pairs.plot(kind="barh", figsize=(10,5), color="orange")
    plt.title("Top 10 Batting Partnerships in IPL")
    plt.show()

def analyze_team_performance_over_time(matches):
    """Analyze and plot team performance over time (seasonal wins)."""
    matches['season'] = matches['season'].astype(str)
    season_wins = matches.groupby(['season', 'winner']).size().unstack(fill_value=0)
    season_wins.plot(kind='line', figsize=(12, 6))
    plt.title('Team Performance Over Time')
    plt.ylabel('Number of Wins')
    plt.xlabel('Season')
    plt.legend(title="Team", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def main():
    # Load datasets
    matches_path = "matches.csv"
    deliveries_path = "deliveries.csv"

    try:
        matches, deliveries = load_data(matches_path, deliveries_path)
    except FileNotFoundError as e:
        print(e)
        return

    # Preprocess the data
    preprocess_data(matches, deliveries)

    # Perform analyses
    plot_match_outcome(matches)
    plot_venue_performance(matches)
    plot_player_performance(deliveries)
    plot_run_rate(deliveries)
    plot_team_comparison(matches)
    plot_batting_partnerships(deliveries)
    analyze_team_performance_over_time(matches)

    print("Analysis Completed Successfully!")

if __name__ == "__main__":
    main()
