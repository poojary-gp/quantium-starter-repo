# import pandas as pd

# # Load processed data
# df = pd.read_csv("data/processed_sales.csv")

# # Convert date column to datetime
# df["date"] = pd.to_datetime(df["date"])

# # Define the price increase date
# price_increase_date = pd.to_datetime("2021-01-15")

# # Split data into before and after
# before = df[df["date"] < price_increase_date]
# after = df[df["date"] >= price_increase_date]

# # Calculate total sales
# before_sales = before["sales"].sum()
# after_sales = after["sales"].sum()

# print("Total Sales BEFORE 15 Jan 2021:", before_sales)
# print("Total Sales AFTER 15 Jan 2021:", after_sales)

# if before_sales > after_sales:
#     print(" Sales were HIGHER before the price increase.")
# else:
#     print(" Sales were HIGHER after the price increase.")


import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("data/processed_sales.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Define the price increase date
price_increase_date = pd.to_datetime("2021-01-15")

# Split data into before and after
before = df[df["date"] < price_increase_date]
after = df[df["date"] >= price_increase_date]

# Calculate total sales
before_sales = before["sales"].sum()
after_sales = after["sales"].sum()

print("Total Sales BEFORE 15 Jan 2021:", before_sales)
print("Total Sales AFTER 15 Jan 2021:", after_sales)

if before_sales > after_sales:
    print("Sales were HIGHER before the price increase.")
else:
    print("Sales were HIGHER after the price increase.")

# ---- VISUALIZATION ----
# Aggregate daily sales
daily_sales = df.groupby("date")["sales"].sum()

plt.figure(figsize=(12,6))
plt.plot(daily_sales.index, daily_sales.values, label="Daily Sales", color="green")

# Add vertical line for price increase
plt.axvline(price_increase_date, color="red", linestyle="--", label="Price Increase (15 Jan 2021)")

plt.title("Pink Morsel Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.legend()
plt.tight_layout()
plt.show()

