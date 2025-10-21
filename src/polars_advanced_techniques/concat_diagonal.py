# Concatenates DataFrames with mismatched columns using Polars diagonal strategy.

import polars as pl

df1 = pl.DataFrame({"x": [1, 2], "y": [3, 4]})
df2 = pl.DataFrame({"y": [5, 6], "z": [7, 8]})

result = pl.concat([df1, df2], how="diagonal")

print(result)
