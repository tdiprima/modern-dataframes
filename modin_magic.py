"""
PriceCruncher: Calculates totals from prices and quantities
Inspired by: https://python.plainenglish.io/these-5-python-libraries-took-my-project-from-it-works-to-this-is-genius-15716787e36f
"""

import modin.pandas as pd
import numpy as np


def generate_sample_data(num_rows: int = 1000) -> pd.DataFrame:
    """
    Generate sample data with random prices and quantities.
    
    Args:
        num_rows (int): Number of rows to generate. Defaults to 1000.
    
    Returns:
        pd.DataFrame: A Modin DataFrame with sample data.
    """
    np.random.seed(42)  # For reproducibility
    data = {
        "price": np.random.uniform(10, 100, num_rows),  # Random prices between 10 and 100
        "quantity": np.random.randint(1, 50, num_rows)  # Random quantities between 1 and 50
    }
    return pd.DataFrame(data)


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process the data by adding a new column 'total'.
    
    Args:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame with the added 'total' column.
    """
    df["total"] = df["price"] * df["quantity"]
    return df


def main():
    # Generate and save sample data to CSV
    sample_df = generate_sample_data()
    sample_df.to_csv("big_data.csv", index=False)
    
    # Read CSV and process data
    df = pd.read_csv("big_data.csv")
    processed_df = process_data(df)
    
    # Display the first few rows
    print(processed_df.head())


if __name__ == "__main__":
    main()
