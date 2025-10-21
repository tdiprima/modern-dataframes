# Handles nested struct data in Polars by extracting fields from metadata.

import polars as pl

df = pl.DataFrame({
    "user_id": [1, 2, 3],
    "metadata": [
        {"location": "Boston", "age": 27},
        {"location": "Seattle", "age": 32},
        {"location": "Denver", "age": 29}
    ]
})

result = df.with_columns([
    pl.col("metadata").struct.field("location").alias("location"),
    pl.col("metadata").struct.field("age").alias("age")
])

print(result)
