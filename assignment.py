# ================================================
# 📊 Python Assignment: Data Analysis with Pandas & Visualization with Matplotlib
# ================================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ---------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------
try:
    # Load CSV file (replace with your dataset if needed)
    file_path = r"C:\Users\ADMIN\Downloads\sales_data.csv"
    df = pd.read_csv(file_path)

    print("✅ Dataset Loaded Successfully!\n")
    print("🔹 First 5 rows:")
    print(df.head(), "\n")

    print("🔹 Info:")
    print(df.info(), "\n")

    print("🔹 Missing Values:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (fill or drop missing values)
    df.fillna(0, inplace=True)

except FileNotFoundError:
    print("❌ Error: File not found. Please check the file path.")
except Exception as e:
    print(f"❌ An error occurred: {e}")

# ---------------------------
# Task 2: Basic Data Analysis
# ---------------------------

print("\n📊 Summary Statistics:")
print(df.describe(), "\n")

# Example: Grouping by Product to find average revenue
if "Product" in df.columns:
    avg_revenue_by_product = df.groupby("Product")["Revenue ($)"].mean()
    print("🔹 Average Revenue by Product:")
    print(avg_revenue_by_product, "\n")

# Patterns / insights
total_revenue = df["Revenue ($)"].sum()
best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_selling_qty = df.groupby("Product")["Quantity Sold"].sum().max()

print(f"💡 Total Revenue: ${total_revenue:,}")
print(f"💡 Best-Selling Product: {best_selling_product} ({best_selling_qty} units)")

# ---------------------------
# Task 3: Data Visualization
# ---------------------------

# 1. Line chart: Daily sales trend
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    daily_sales = df.groupby("Date")["Revenue ($)"].sum()

    plt.figure(figsize=(8,5))
    plt.plot(daily_sales.index, daily_sales.values, marker="o", linestyle="--", color="blue")
    plt.title("📈 Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 2. Bar chart: Average revenue by product
if "Product" in df.columns:
    avg_revenue_by_product.plot(kind="bar", color="green", figsize=(7,5))
    plt.title("📊 Average Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.show()

# 3. Histogram: Distribution of Quantity Sold
if "Quantity Sold" in df.columns:
    df["Quantity Sold"].plot(kind="hist", bins=10, color="skyblue", edgecolor="black", figsize=(7,5))
    plt.title("📊 Distribution of Quantity Sold")
    plt.xlabel("Quantity Sold")
    plt.tight_layout()
    plt.show()

# 4. Scatter plot: Quantity vs Revenue
if "Quantity Sold" in df.columns and "Revenue ($)" in df.columns:
    plt.figure(figsize=(7,5))
    plt.scatter(df["Quantity Sold"], df["Revenue ($)"], alpha=0.7, color="purple")
    plt.title("🔵 Quantity Sold vs Revenue")
    plt.xlabel("Quantity Sold")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.show()

# ---------------------------
# Findings / Observations
# ---------------------------
print("\n🔎 Observations:")
print("- The best-selling product is", best_selling_product, "with", best_selling_qty, "units.")
print("- Total revenue generated is $", format(total_revenue, ","), ".")
print("- The daily sales trend shows revenue fluctuations across different days.")
print("- Products vary significantly in revenue contribution, highlighting demand differences.")

