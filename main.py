import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the correct paths to the data files on your Desktop
matches_path = r'C:\Users\poorn\OneDrive\Desktop\IPL-INT\matches.csv'
deliveries_path = r'C:\Users\poorn\OneDrive\Desktop\IPL-INT\deliveries.csv'

# Check if files exist
if not os.path.exists(matches_path) or not os.path.exists(deliveries_path):
    print(f"Error: One or both data files not found!\nMatches: {matches_path}\nDeliveries: {deliveries_path}")
    exit()

# Load the IPL datasets
matches_df = pd.read_csv(matches_path)
deliveries_df = pd.read_csv(deliveries_path)

# Convert date column to datetime format
if 'date' in matches_df.columns:
    matches_df['date'] = pd.to_datetime(matches_df['date'])
else:
    print("Warning: 'date' column missing in matches.csv!")

# 1️⃣ Match Outcomes Over Different Years (Already Done)
def match_outcome_analysis():
    """Visualizes match outcomes over different years."""
    plt.figure(figsize=(12, 6))
    sns.countplot(x=matches_df['season'], hue=matches_df['winner'], palette='coolwarm')
    plt.title("Match Outcomes Across Different Years")
    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.xticks(rotation=45)
    plt.legend(title="Winning Team", bbox_to_anchor=(1, 1))
    plt.show()

# 2️⃣ Player Performance - Runs Distribution
def player_performance(player_name):
    """Analyzes and visualizes an individual player's runs scored distribution."""
    if 'batter' not in deliveries_df.columns:
        print("Error: 'batter' column missing in deliveries dataset!")
        return
    
    player_data = deliveries_df[deliveries_df['batter'] == player_name]
    if player_data.empty:
        print(f"No data found for player: {player_name}")
        return
    
    plt.figure(figsize=(10, 5))
    sns.histplot(player_data['batsman_runs'], bins=10, kde=True, color='blue')
    plt.title(f"Performance of {player_name} - Runs Distribution")
    plt.xlabel("Runs Scored")
    plt.ylabel("Frequency")
    plt.show()

# 3️⃣ Team Comparison - Total Matches Won
def team_comparison():
    """Compares team performances in terms of total wins."""
    if 'winner' not in matches_df.columns:
        print("Error: 'winner' column missing in matches dataset!")
        return

    team_wins = matches_df['winner'].value_counts()
    plt.figure(figsize=(12, 6))
    team_wins.plot(kind='bar', colormap='viridis')
    plt.title("Total Matches Won by Teams")
    plt.xlabel("Teams")
    plt.ylabel("Number of Matches Won")
    plt.xticks(rotation=45)
    plt.show()

# 4️⃣ Venue Performance - Matches Won at Different Venues
def venue_performance():
    """Evaluates match outcomes across different venues."""
    if 'venue' not in matches_df.columns or 'winner' not in matches_df.columns:
        print("Error: 'venue' or 'winner' column missing in matches dataset!")
        return

    plt.figure(figsize=(12, 6))
    venue_wins = matches_df.groupby('venue')['winner'].count().sort_values(ascending=False)
    venue_wins.plot(kind='bar', colormap='coolwarm')
    plt.title("Wins at Different Venues")
    plt.xlabel("Venue")
    plt.ylabel("Number of Wins")
    plt.xticks(rotation=90)
    plt.show()

# 5️⃣ Run Rate Analysis - Average Run Rates of Teams
def run_rate_analysis():
    """Visualizes average run rates of different teams."""
    if 'over' not in deliveries_df.columns or 'total_runs' not in deliveries_df.columns:
        print("Error: Missing 'over' or 'total_runs' columns in deliveries dataset!")
        return

    deliveries_df['run_rate'] = deliveries_df['total_runs'] / (deliveries_df['over'] + 1)  # Avoid division by zero
    avg_run_rate = deliveries_df.groupby('batting_team')['run_rate'].mean().sort_values()

    plt.figure(figsize=(10, 5))
    avg_run_rate.plot(kind='barh', colormap='plasma')
    plt.title("Average Run Rate of Teams")
    plt.xlabel("Run Rate")
    plt.ylabel("Teams")
    plt.show()

# 6️⃣ Best Batting Partnerships
def best_batting_partnership():
    """Identifies top batting partnerships."""
    if 'batter' not in deliveries_df.columns or 'non_striker' not in deliveries_df.columns:
        print("Error: Missing 'batter' or 'non_striker' columns in deliveries dataset!")
        return

    partnerships = deliveries_df.groupby(['batter', 'non_striker'])['total_runs'].sum().reset_index()
    top_partnerships = partnerships.sort_values(by='total_runs', ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_partnerships, x='total_runs', y=top_partnerships['batter'] + " & " + top_partnerships['non_striker'], palette='magma')
    plt.title("Top 10 Batting Partnerships")
    plt.xlabel("Runs Scored")
    plt.ylabel("Partnerships")
    plt.show()

# Debugging - Print dataset columns
print("Matches Dataset Columns:", matches_df.columns.tolist())
print("Deliveries Dataset Columns:", deliveries_df.columns.tolist())

# Run all visualizations
match_outcome_analysis()  # ✅ Answer Q1
player_performance("Virat Kohli")  # 📊 Answer Q2
team_comparison()  # ⚔️ Answer Q3
venue_performance()  # 🏟️ Answer Q4
run_rate_analysis()  # 📈 Answer Q5
best_batting_partnership()  # 🏏 Answer Q6
