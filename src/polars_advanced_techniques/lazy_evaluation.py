# Demonstrates lazy evaluation in Polars for optimized data processing.
# It reads a CSV file, filters revenue greater than 1200, groups by region, and sums revenue.

import polars as pl

# Generate sample sales.csv data
sales_data = pl.DataFrame({
    "region": ["North", "South", "East", "West", "North", "South"],
    "revenue": [800, 1500, 1200, 2000, 900, 1300]
})
sales_data.write_csv("sales.csv")

# Optimized lazy execution
result = (
    pl.scan_csv("sales.csv")
    .filter(pl.col("revenue") > 1200)
    .group_by("region")
    .agg(pl.col("revenue").sum())
    .collect()
)

print(result)
