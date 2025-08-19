import pandas as pd

# Load all three CSVs
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df1, df2, df3])

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Convert price from "$3.00" → 3.00
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales
df["sales"] = df["quantity"] * df["price"]

# Keep only needed columns
final_df = df[["sales", "date", "region"]]

# Save processed data
final_df.to_csv("data/processed_sales.csv", index=False)

print("Processed data saved to data/processed_sales.csv")
