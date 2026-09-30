import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/cleaned_ecommerce_sales.csv")

# Create SQLite database
connection = sqlite3.connect("data/ecommerce.db")

# Create SQL table
df.to_sql(
    "ecommerce_sales",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Table created: ecommerce_sales")

connection.close()