import pandas as pd

# File paths
raw_file = "data/raw/nyc_311_2024_monthly_sample.csv"
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"

# Load the raw data
df = pd.read_csv(raw_file)

original_rows = df.shape[0]

print("Raw data loaded successfully.")
print("Original rows:", original_rows)


# Convert date columns to datetime
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


# Remove rows where created_date or closed_date could not be read
df = df.dropna(subset=["created_date", "closed_date"])

rows_after_date_cleaning = df.shape[0]

print("Rows after date cleaning:", rows_after_date_cleaning)


# Calculate resolution time
df["resolution_time_hours"] = (
    df["closed_date"] - df["created_date"]
).dt.total_seconds() / 3600

df["resolution_time_days"] = df["resolution_time_hours"] / 24

print("Resolution time columns created.")


# Remove rows with negative resolution time
df = df[df["resolution_time_hours"] >= 0]

rows_after_time_cleaning = df.shape[0]

print("Rows after removing negative resolution times:", rows_after_time_cleaning)


# Keep only the five main NYC boroughs
valid_boroughs = [
    "BRONX",
    "BROOKLYN",
    "MANHATTAN",
    "QUEENS",
    "STATEN ISLAND"
]

df = df[df["borough"].isin(valid_boroughs)]

rows_after_borough_filter = df.shape[0]

print("Rows after borough filtering:", rows_after_borough_filter)


# Create extra date columns for analysis
df["created_year"] = df["created_date"].dt.year
df["created_month"] = df["created_date"].dt.month
df["created_month_name"] = df["created_date"].dt.month_name()
df["created_day_of_week"] = df["created_date"].dt.day_name()

print("Date feature columns created.")


# Save the cleaned data
df.to_csv(cleaned_file, index=False)

cleaned_rows = df.shape[0]
rows_removed = original_rows - cleaned_rows

print("\nCleaning summary")
print("-" * 40)
print("Original rows:", original_rows)
print("Cleaned rows:", cleaned_rows)
print("Rows removed:", rows_removed)
print("Cleaned file saved to:", cleaned_file)



