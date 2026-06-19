import pandas as pd

# File path for the raw sample data
raw_file = "data/raw/nyc_311_2024_closed_sample.csv"

# Load the raw data so we can inspect it before cleaning
df = pd.read_csv(raw_file)

print("NYC 311 raw data loaded successfully.")


# Check the size of the dataset
print("\nRows and columns:")
print(df.shape)


# Preview the first few rows to understand what the data looks like
print("\nFirst 5 rows:")
print(df.head())


# Print column names so we know which fields are available for analysis
print("\nColumn names:")
print(df.columns.tolist())


# Show data types and non-null counts for each column
print("\nDataset info:")
df.info()


# Check missing values before deciding what needs cleaning
print("\nMissing values by column:")
print(df.isna().sum())


# Check the most common complaint types
print("\nTop 10 complaint types:")
print(df["complaint_type"].value_counts().head(10))


# Check complaint volume by borough
print("\nComplaint counts by borough:")
print(df["borough"].value_counts())