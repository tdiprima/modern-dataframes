# Builds custom strings using Polars concat_str with conditional logic for handling missing data.

import polars as pl

df = pl.DataFrame({
    "first_name": ["Bear", "Jordan", None],
    "last_name": ["Brown", "Lee", "Taylor"],
    "title": ["Mr.", None, "Dr."]
})

result = df.with_columns(
    pl.concat_str([
        pl.when(pl.col("title").is_not_null())
        .then(pl.concat_str([pl.col("title"), pl.lit(" ")]))
        .otherwise(pl.lit("")),
        pl.col("first_name").fill_null("Unknown"),
        pl.lit(" "),
        pl.col("last_name")
    ]).alias("full_name")
)

print(result)
