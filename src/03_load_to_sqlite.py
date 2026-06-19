import sqlite3
import pandas as pd

# File paths
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"
database_file = "data/processed/nyc_311.db"

# Load the cleaned data
df = pd.read_csv(cleaned_file)

print("Cleaned data loaded successfully.")
print("Rows and columns:", df.shape)

# Connect to a local SQLite database
connection = sqlite3.connect(database_file)

# Save the cleaned data as a table in SQLite
df.to_sql(
    "nyc_311_requests",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Data loaded into SQLite successfully.")
print("Database saved to:", database_file)
print("Table name: nyc_311_requests")