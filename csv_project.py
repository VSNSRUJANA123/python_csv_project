import pandas as pd

# Load dataset
try:
    df = pd.read_csv(r"D:\srujana python projects\data\sales_data.csv")
    print(df.head())
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty. Please add some data.")

# Data cleaning - remove null values
df = df.dropna()

# Filtering - sales above 1000
high_sales = df[df['Sales'] > 1000]

# Summarization
print("Total Rows:", len(df))
print("Average Sales:", df['Sales'].mean())
print("Top 5 Customers by Sales:")
print(df.groupby("Customer")['Sales'].sum().sort_values(ascending=False).head())

# Visualization (optional if matplotlib installed)
import matplotlib.pyplot as plt
df['Sales'].hist(bins=20)
plt.title("Sales Distribution")
plt.show()

