import dataiku
import pandas as pd
import numpy as np

ds = dataiku.Dataset("clean_housing_data")
df = ds.get_dataframe()

# Feature engineering
df["rooms_per_household"] = df["AveRooms"] / df["HouseAge"].replace(0, 1)
df["bedrooms_per_room"] = df["AveBedrms"] / df["AveRooms"].replace(0, 1)
df["population_per_household"] = df["Population"] / df["HouseAge"].replace(0, 1)

# Replace invalid values
df.replace([np.inf, -np.inf], 0, inplace=True)
df = df.fillna(0)

out = dataiku.Dataset("features_housing_data")
out.write_with_schema(df)
