# Uses Polars SQL to perform joins and conditional logic on DataFrames.

import polars as pl

df1 = pl.DataFrame({"id": [1, 2, 3], "value": [15, 25, 35]})
df2 = pl.DataFrame({"id": [1, 2, 4], "category": ["X1", "Y2", "Z3"]})

result = pl.sql("""
    SELECT
        a.id,
        a.value,
        b.category,
        CASE
            WHEN a.value > 20 THEN 'High'
            ELSE 'Low'
        END as segment
    FROM df1 a
    LEFT JOIN df2 b ON a.id = b.id
    WHERE a.value > 10
""").collect()

print(result)
