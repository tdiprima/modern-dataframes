# Uses Polars window functions to compute running totals, ranks, and percentages per product.

import polars as pl

df = pl.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-01-03"] * 3,
    "product": ["X", "X", "X", "Y", "Y", "Y", "Z", "Z", "Z"],
    "sales": [120, 180, 240, 90, 140, 110, 210, 190, 230]
})

result = df.with_columns([
    pl.col("sales").cum_sum().over("product").alias("running_total"),
    pl.col("sales").rank().over("product").alias("rank"),
    (pl.col("sales") / pl.col("sales").sum().over("product") * 100).alias("pct_of_product_sales")
])

print(result)
