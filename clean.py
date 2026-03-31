import dataiku
import pandas as pd
import numpy as np

ds = dataiku.Dataset("raw_housing_data")
df = ds.get_dataframe()

# Remove duplicates
df = df.drop_duplicates()

# Convert all columns to numeric safely
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing values
df = df.fillna(df.median(numeric_only=True))

# Remove invalid rows
df = df[df["price"] > 0]

# Remove extreme outliers (optional but good)
df = df[df["price"] < df["price"].quantile(0.99)]

# Final safety
df.replace([np.inf, -np.inf], 0, inplace=True)

out = dataiku.Dataset("clean_housing_data")
out.write_with_schema(df)
