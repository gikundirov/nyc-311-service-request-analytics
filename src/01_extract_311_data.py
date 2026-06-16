import pandas as pd

# Load the CSV file
df = pd.read_csv("data/raw/nyc_311_2024_closed_sample.csv")

# Confirm it loaded
print("NYC 311 data loaded successfully!")

# Basic overview
print("\nRows and columns:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset info:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nTop 10 complaint types:")
print(df["complaint_type"].value_counts().head(10))

print("\nComplaint counts by borough:")
print(df["borough"].value_counts())