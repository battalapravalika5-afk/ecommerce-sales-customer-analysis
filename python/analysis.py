# E-Commerce Sales & Customer Analysis
# Run this file from the project root.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("data/ecommerce_sales.csv")
print("Shape:", df.shape)
print(df.head())

# 2. Basic inspection
print(df.info())
print(df.describe(include="all"))

# 3. Data quality checks
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# 4. Cleaning
df = df.drop_duplicates().copy()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Region"] = df["Region"].fillna("Unknown")
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")

# 5. Feature engineering
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Profit_Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"] * 100, 0)

# 6. KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = df["Sales"].mean()

print("\nKEY KPIs")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Average Order Value:", round(avg_order_value, 2))

# 7. Category analysis
category_analysis = df.groupby("Category").agg(
    Orders=("Order_ID", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

print("\nCategory Analysis:")
print(category_analysis)

# 8. Regional analysis
region_analysis = df.groupby("Region").agg(
    Orders=("Order_ID", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Sales", ascending=False)

print("\nRegional Analysis:")
print(region_analysis)

# 9. Top products
top_products = df.groupby("Product").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False).head(10)

print("\nTop 10 Products:")
print(top_products)

# 10. Top customers
top_customers = df.groupby("Customer_ID").agg(
    Orders=("Order_ID", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Sales", ascending=False).head(10)

print("\nTop 10 Customers:")
print(top_customers)

# 11. Monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

# 12. Visualizations
plt.figure(figsize=(9, 5))
category_analysis["Sales"].sort_values().plot(kind="barh")
plt.title("Sales by Category")
plt.xlabel("Sales")
plt.tight_layout()
plt.close()

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.close()

plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category")
plt.title("Discount vs Profit")
plt.tight_layout()
plt.close()

plt.figure(figsize=(8, 5))
sns.barplot(data=region_analysis.reset_index(), x="Region", y="Sales")
plt.title("Sales by Region")
plt.tight_layout()
plt.close()

# 13. Export cleaned data for SQL
df.to_csv("data/cleaned_ecommerce_sales.csv", index=False)

print("\nAnalysis completed. Cleaned data exported.")
