# Computes rolling statistics on time-series data using Polars.

import polars as pl

weather_data = pl.DataFrame({
    "day": pl.date_range(start="2024-01-01", end="2024-01-10", interval="1d", eager=True),
    "temp_fahrenheit": [68, 72, 66, 74, 77, 75, 72, 70, 68, 73]
})

weather_stats = weather_data.with_columns([
    pl.col("temp_fahrenheit")
    .rolling_mean(window_size=3, min_periods=1)
    .alias("three_day_temp_avg"),
    pl.col("temp_fahrenheit")
    .rolling_std(window_size=3)
    .alias("temp_fluctuation")
])

print(weather_stats)
