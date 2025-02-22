import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Data Preprocessing
matches.dropna(inplace=True)
deliveries.fillna(0, inplace=True)
matches["date"] = pd.to_datetime(matches["date"])

# Match Outcome Analysis
team_wins = matches["winner"].value_counts()
plt.figure(figsize=(10,5))
sns.barplot(x=team_wins.index, y=team_wins.values, palette="viridis")
plt.xticks(rotation=90)
plt.title("Total Wins by Each Team")
plt.show()

# Venue Performance Analysis
venue_counts = matches["venue"].value_counts().head(10)
sns.barplot(x=venue_counts.values, y=venue_counts.index, palette="coolwarm")
plt.title("Top 10 Venues with Most Matches")
plt.show()

# Player Performance Analysis
top_batsmen = deliveries.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette="magma")
plt.title("Top 10 Run Scorers in IPL")
plt.show()

top_bowlers = deliveries[deliveries["dismissal_kind"].notnull()].groupby("bowler")["dismissal_kind"].count().sort_values(ascending=False).head(10)
sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette="plasma")
plt.title("Top 10 Wicket-Takers in IPL")
plt.show()

# Run Rate & Scoring Trends
team_run_rate = deliveries.groupby("batting_team")["total_runs"].sum() / deliveries.groupby("batting_team")["over"].nunique()
team_run_rate.sort_values(ascending=False).plot(kind="bar", figsize=(10,5), color="teal")
plt.title("Average Run Rate per Team")
plt.show()

# Team Comparison
win_percentage = (matches["winner"].value_counts() / matches["winner"].count()) * 100
sns.barplot(x=win_percentage.index, y=win_percentage.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Win Percentage of Teams")
plt.show()

# Best Batting Partnerships
batting_pairs = deliveries.groupby(["batsman", "non_striker"])['total_runs'].sum().sort_values(ascending=False).head(10)
batting_pairs.plot(kind="barh", figsize=(10,5), color="orange")
plt.title("Top 10 Batting Partnerships in IPL")
plt.show()

print("Analysis Completed Successfully!")
