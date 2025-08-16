"""
PriceCruncher: Calculates totals from prices and quantities
Adapted from: https://python.plainenglish.io/these-5-python-libraries-took-my-project-from-it-works-to-this-is-genius-15716787e36f
"""
import modin.pandas as pd
import numpy as np

# Create sample data
data = {
    "price": np.random.uniform(10, 100, 1000),  # Random prices between 10 and 100
    "quantity": np.random.randint(1, 50, 1000)  # Random quantities between 1 and 50
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("big_data.csv", index=False)

# Now run your original code
df = pd.read_csv("big_data.csv")
df["total"] = df["price"] * df["quantity"]

print(df.head())
