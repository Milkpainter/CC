"""
Tennis Matches Dataset - 500+ Real Matches  
Complete professional tennis match records with analysis functions
"""

import json
import pandas as pd
from pathlib import Path
from collections import Counter

def load_matches_data():
    """Load the complete matches from JSON file"""
    json_file = Path(__file__).parent / 'matches_data.json'
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_matches_df():
    """Load matches as pandas DataFrame"""
    return pd.DataFrame(load_matches_data())

def get_player_matches(player_name):
    """Get all matches for a specific player"""
    df = load_matches_df()
    return df[(df['Player1'] == player_name) | (df['Player2'] == player_name)]

def get_tournament_matches(tournament):
    """Get matches from specific tournament"""
    df = load_matches_df()
    return df[df['Tournament'] == tournament]

def get_head_to_head(player1, player2):
    """Get head-to-head record between two players"""
    df = load_matches_df()
    h2h = df[((df['Player1'] == player1) & (df['Player2'] == player2)) |
             ((df['Player1'] == player2) & (df['Player2'] == player1))]
    return h2h

def get_tournaments():
    """Get all unique tournaments"""
    df = load_matches_df()
    return sorted(df['Tournament'].unique().tolist())

def get_all_players():
    """Get all unique players"""
    df = load_matches_df()
    players = set(df['Player1'].tolist() + df['Player2'].tolist())
    return sorted(list(players))

def print_summary():
    """Print dataset summary"""
    df = load_matches_df()
    all_players = get_all_players()
    print(f"Total Matches: {len(df)}")
    print(f"Unique Players: {len(all_players)}")
    print(f"Unique Tournaments: {df['Tournament'].nunique()}")
    print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"Men's Singles: {len(df[df['Category'] == 'Men\'s Singles'])}")
    print(f"Women's Singles: {len(df[df['Category'] == 'Women\'s Singles'])}")

if __name__ == "__main__":
    print_summary()