import dataiku
import pandas as pd
import numpy as np

# Read input dataset
input_ds = dataiku.Dataset("raw_house_data")
df = input_ds.get_dataframe()

# Standardize column names
df.columns = [c.strip().lower() for c in df.columns]

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where target is missing
df = df.dropna(subset=["price"])

# Fill missing numeric columns with median
numeric_cols = ["area_sqft", "bedrooms", "bathrooms", "property_age", "garage_spaces"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

# Fill missing categorical columns
categorical_cols = ["location", "has_garden", "near_metro"]
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).replace(["nan", "None"], np.nan)
        df[col] = df[col].fillna("Unknown")

# Normalize Yes/No columns
for col in ["has_garden", "near_metro"]:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()
        df[col] = df[col].replace({
            "Y": "Yes",
            "N": "No",
            "True": "Yes",
            "False": "No"
        })

# Basic outlier filtering (optional, simple rule)
if "area_sqft" in df.columns:
    df = df[df["area_sqft"] > 200]

if "price" in df.columns:
    df = df[df["price"] > 50000]

# Write output
output_ds = dataiku.Dataset("clean_house_data")
output_ds.write_with_schema(df)
