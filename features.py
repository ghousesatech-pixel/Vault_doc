import dataiku
import pandas as pd
import numpy as np

input_ds = dataiku.Dataset("clean_house_data")
df = input_ds.get_dataframe()

# Feature 1: price-independent engineered features
df["total_rooms"] = df["bedrooms"] + df["bathrooms"]

# Feature 2: area per bedroom
df["area_per_bedroom"] = df["area_sqft"] / df["bedrooms"].replace(0, 1)

# Feature 3: new property flag
df["is_new_property"] = (df["property_age"] <= 5).astype(int)

# Feature 4: convert Yes/No flags to numeric
df["has_garden_flag"] = df["has_garden"].map({"Yes": 1, "No": 0, "Unknown": 0}).fillna(0)
df["near_metro_flag"] = df["near_metro"].map({"Yes": 1, "No": 0, "Unknown": 0}).fillna(0)

# One-hot encode location
if "location" in df.columns:
    df = pd.get_dummies(df, columns=["location"], prefix="loc")

# Drop columns not needed for modeling
drop_cols = ["property_id", "has_garden", "near_metro"]
existing_drop_cols = [c for c in drop_cols if c in df.columns]
df = df.drop(columns=existing_drop_cols)

output_ds = dataiku.Dataset("features_house_data")
output_ds.write_with_schema(df)
