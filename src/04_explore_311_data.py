import pandas as pd

# Load cleaned data
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"
df = pd.read_csv(cleaned_file)

# Check dataset size
print("Cleaned NYC 311 data loaded successfully!")
print("Rows and columns:")
print(df.shape)

# Count complaints by borough
print("\nComplaint counts by borough:")
print(df["borough"].value_counts())

# Count top complaint types
print("\nTop 10 complaint types:")
print(df["complaint_type"].value_counts().head(10))

# Calculate average resolution time by borough
avg_time_by_borough = (
    df.groupby("borough")["resolution_time_hours"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage resolution time by borough:")
print(avg_time_by_borough.round(2))

# Calculate average resolution time by complaint type
avg_time_by_type = (
    df.groupby("complaint_type")["resolution_time_hours"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 slowest complaint types:")
print(avg_time_by_type.round(2))

# Find complaint types that are both common and slow
type_summary = (
    df.groupby("complaint_type")
    .agg(
        complaint_count=("unique_key", "count"),
        avg_resolution_hours=("resolution_time_hours", "mean")
    )
    .sort_values("avg_resolution_hours", ascending=False)
)

common_slow_types = type_summary[type_summary["complaint_count"] >= 100].head(10)

print("\nCommon complaint types with slowest average resolution time:")
print(common_slow_types.round(2))


# Count complaints by month
monthly_complaints = (
    df.groupby("created_month_name")["unique_key"]
    .count()
    .sort_values(ascending=False)
)

print("\nComplaint counts by month:")
print(monthly_complaints)


# Calculate median resolution time by month
median_time_by_month = (
    df.groupby("created_month_name")["resolution_time_hours"]
    .median()
    .sort_values(ascending=False)
)

print("\nMedian resolution time by month:")
print(median_time_by_month.round(2))


# Calculate median resolution time by borough
median_time_by_borough = (
    df.groupby("borough")["resolution_time_hours"]
    .median()
    .sort_values(ascending=False)
)

print("\nMedian resolution time by borough:")
print(median_time_by_borough.round(2))


# Calculate median resolution time by complaint type
median_time_by_type = (
    df.groupby("complaint_type")["resolution_time_hours"]
    .median()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 complaint types by median resolution time:")
print(median_time_by_type.round(2))


# Save summary tables for later use
type_summary.to_csv("data/processed/complaint_type_summary.csv")
avg_time_by_borough.to_csv("data/processed/avg_time_by_borough.csv")
monthly_complaints.to_csv("data/processed/monthly_complaints.csv")

print("\nSummary files saved to data/processed/")