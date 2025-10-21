# Applies a custom function using map_batches in Polars to calculate percentiles on list columns.

import numpy as np
import polars as pl

df = pl.DataFrame({
    "values": [[2, 4, 6], [3, 5, 7], [1, 8, 9]]
})


def calculate_percentile(series):
    return pl.Series([np.percentile(x, 80) for x in series])


result = df.with_columns(
    pl.col("values").map_batches(calculate_percentile, return_dtype=pl.Float64).alias("p80")
)

print(result)
