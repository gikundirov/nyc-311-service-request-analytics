import pandas as pd

raw_file = "data/raw/nyc_311_2024_monthly_sample.csv"
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"

# Load raw CSV
df = pd.read_csv(raw_file)
# Save original row count
original_rows = df.shape[0]

print("Raw data loaded successfully!")
print("Original rows:")
print(original_rows)

# Convert date columns from text to datetime
df["created_date"] = pd.to_datetime(
    df["created_date"],
    format="mixed",
    errors="coerce"
)

df["closed_date"] = pd.to_datetime(
    df["closed_date"],
    format="mixed",
    errors="coerce"
)

# Remove rows with missing created_date or closed_date
df = df.dropna(subset=["created_date", "closed_date"])

rows_after_date_cleaning = df.shape[0]

print("Rows after date cleaning:")
print(rows_after_date_cleaning)

# Calculate how long each complaint took to close
df["resolution_time_hours"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 3600

# Also calculate resolution time in days
df["resolution_time_days"] = df["resolution_time_hours"] / 24

print("Resolution time columns created successfully!")

# Remove rows where resolution time is negative
df = df[df["resolution_time_hours"] >= 0]

rows_after_time = df.shape[0]

print("Rows after removing invalid resolution times:")
print(rows_after_time)

# Keep only valid NYC boroughs
valid_boroughs = ["BRONX", "BROOKLYN", "MANHATTAN", "QUEENS", "STATEN ISLAND"]

df = df[df["borough"].isin(valid_boroughs)]

rows_after_boroughs = df.shape[0]

print("Rows after borough filtering:")
print(rows_after_boroughs)

# Create date features for future analysis
df["created_year"] = df["created_date"].dt.year
df["created_month"] = df["created_date"].dt.month
df["created_month_name"] = df["created_date"].dt.month_name()
df["created_day_of_week"] = df["created_date"].dt.day_name()

print("Date feature columns created successfully!")

# Save cleaned data
df.to_csv(cleaned_file, index=False)

print("Cleaned file saved to:", cleaned_file)
print("Saved file:")
print(cleaned_file)

# Final cleaning summary
clean_rows = df.shape[0]
rows_removed = original_rows - clean_rows

print("\nCleaning summary")
print("-" * 40)
print("Original rows:", original_rows)
print("Cleaned rows:", clean_rows)
print("Rows removed:", rows_removed)
print("Cleaned file saved to:", cleaned_file)



