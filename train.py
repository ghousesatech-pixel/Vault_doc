import dataiku
import pandas as pd
from sklearn.model_selection import train_test_split

ds = dataiku.Dataset("features_housing_data")
df = ds.get_dataframe()

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

dataiku.Dataset("train_data").write_with_schema(train_df)
dataiku.Dataset("test_data").write_with_schema(test_df)



mkdir -p mirror/registry.terraform.io/ratcliffm/pyscript/1.0.0/linux_amd64
cp bin/terraform-provider-pyscript_v1.0.0 mirror/registry.terraform.io/ratcliffm/pyscript/1.0.0/linux_amd64/
chmod +x mirror/registry.terraform.io/ratcliffm/pyscript/1.0.0/linux_amd64/terraform-provider-pyscript_v1.0.0
find mirror -type f
