import dataiku
import pandas as pd
from sklearn.model_selection import train_test_split

ds = dataiku.Dataset("features_housing_data")
df = ds.get_dataframe()

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

dataiku.Dataset("train_data").write_with_schema(train_df)
dataiku.Dataset("test_data").write_with_schema(test_df)
