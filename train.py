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


Cloned repo and built custom Terraform provider (pyscript) using Go
Configured local filesystem mirror for provider and fixed path structure
Updated dev.tfrc and set TF_CLI_CONFIG_FILE for Terraform to use local provider
Resolved terraform init failure (provider not found issue)
Fixed missing module input (vault_path) in Terraform configuration
Configured Vault access (VAULT_ADDR, VAULT_TOKEN) and resolved authentication error
Corrected Kubernetes namespace to meet RFC 1123 standards (lowercase, no underscores)
Automated environment setup using .bashrc to avoid manual exports

Status: Terraform init successful; plan working after fixes
