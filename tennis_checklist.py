"""
Tennis Prediction Framework Checklist - 500 Components
Complete dataset with helper functions for analysis
"""

import json
import pandas as pd
from pathlib import Path

def load_checklist_data():
    """Load the complete checklist from JSON file"""
    json_file = Path(__file__).parent / 'checklist_data.json'
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_checklist_df():
    """Load checklist as pandas DataFrame"""
    return pd.DataFrame(load_checklist_data())

def get_components_by_category(category):
    """Get all components for a specific category"""
    df = load_checklist_df()
    return df[df['Category'] == category]

def get_categories():
    """Get all unique categories"""
    df = load_checklist_df()
    return sorted(df['Category'].unique().tolist())

def get_real_time_components():
    """Get components available in real-time"""
    df = load_checklist_df()
    return df[df['Real_Time_Available'] == 'Yes']

def get_publicly_available():
    """Get publicly available components"""
    df = load_checklist_df()
    return df[df['Accessibility'] == 'Publicly Available']

def print_summary():
    """Print dataset summary"""
    df = load_checklist_df()
    print(f"Total Components: {len(df)}")
    print(f"Categories: {df['Category'].nunique()}")
    print(f"Real-time Available: {len(df[df['Real_Time_Available'] == 'Yes'])}")
    print(f"Evidence-based: {len(df[df['Evidence_Based'] == 'Yes'])}")

if __name__ == "__main__":
    print_summary()