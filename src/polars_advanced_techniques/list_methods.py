# Analyzes list columns in Polars using various list expressions.

import polars as pl

df = pl.DataFrame({
    "user_id": [1, 2, 3],
    "purchases": [[120, 220, 170], [60], [320, 270, 420, 110]]
})

result = df.with_columns([
    pl.col("purchases").list.len().alias("num_purchases"),
    pl.col("purchases").list.sum().alias("total_spent"),
    pl.col("purchases").list.max().alias("largest_purchase"),
    pl.col("purchases").list.get(0).alias("first_purchase")
])

print(result)
