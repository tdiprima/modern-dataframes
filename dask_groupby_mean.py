# Inspired by: https://medium.com/python-in-plain-english/these-6-python-tools-are-so-good-theyll-make-you-rethink-how-you-write-code-ba007178914f
import dask.dataframe as dd
import numpy as np
import pandas as pd


def create_large_dataset(file_path: str, num_rows: int = 1000000) -> None:
    """
    Create a large dataset with random data and save it to a CSV file.

    Args:
        file_path (str): Path to save the CSV file.
        num_rows (int): Number of rows to generate. Defaults to 1000000.
    """
    np.random.seed(42)  # For reproducibility
    data = {
        "category": np.random.choice(["A", "B", "C", "D"], num_rows),
        "value": np.random.uniform(10, 100, num_rows),
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


def calculate_groupby_mean(
    file_path: str, category_col: str, value_col: str
) -> dd.Series:
    """
    Calculate the mean of a column grouped by another column.

    Args:
    - file_path (str): Path to the large CSV dataset.
    - category_col (str): Name of the column to group by.
    - value_col (str): Name of the column to calculate the mean for.

    Returns:
    - dd.Series: A Dask Series with the groupby mean result.
    """
    try:
        # Read the CSV file into a Dask DataFrame
        df = dd.read_csv(file_path)

        # Ensure the specified columns exist in the DataFrame
        if category_col not in df.columns or value_col not in df.columns:
            raise ValueError("One or both columns do not exist in the DataFrame.")

        # Perform groupby and mean calculation
        result = df.groupby(category_col)[value_col].mean().compute()

        return result

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    file_path = "large_dataset.csv"
    create_large_dataset(file_path)
    category_col = "category"
    value_col = "value"
    result = calculate_groupby_mean(file_path, category_col, value_col)
    print(result)


if __name__ == "__main__":
    main()
