import dataiku
import pandas as pd
from sklearn.model_selection import train_test_split

input_ds = dataiku.Dataset("features_house_data")
df = input_ds.get_dataframe()

# Split data
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Write outputs
dataiku.Dataset("train_data").write_with_schema(train_df)
dataiku.Dataset("test_data").write_with_schema(test_df)
