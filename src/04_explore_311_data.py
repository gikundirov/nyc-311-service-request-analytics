import pandas as pd

# Load the cleaned NYC 311 data
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"
df = pd.read_csv(cleaned_file)

print("Cleaned NYC 311 data loaded successfully.")
print("Rows and columns:")
print(df.shape)


# 1. Complaint counts by borough
complaints_by_borough = df["borough"].value_counts()

print("\nComplaint counts by borough:")
print(complaints_by_borough)


# 2. Top 10 complaint types
top_complaints = df["complaint_type"].value_counts().head(10)

print("\nTop 10 complaint types:")
print(top_complaints)


# 3. Average resolution time by borough
avg_time_by_borough = df.groupby("borough")["resolution_time_hours"].mean()
avg_time_by_borough = avg_time_by_borough.sort_values(ascending=False)

print("\nAverage resolution time by borough:")
print(avg_time_by_borough.round(2).to_string())


# 4. Median resolution time by borough
median_time_by_borough = df.groupby("borough")["resolution_time_hours"].median()
median_time_by_borough = median_time_by_borough.sort_values(ascending=False)

print("\nMedian resolution time by borough:")
print(median_time_by_borough.round(2))


# 5. Slowest complaint types by average resolution time
avg_time_by_type = df.groupby("complaint_type")["resolution_time_hours"].mean()
avg_time_by_type = avg_time_by_type.sort_values(ascending=False).head(10)

print("\nTop 10 slowest complaint types by average resolution time:")
print(avg_time_by_type.round(2))


# 6. Slowest complaint types by median resolution time
median_time_by_type = df.groupby("complaint_type")["resolution_time_hours"].median()
median_time_by_type = median_time_by_type.sort_values(ascending=False).head(10)

print("\nTop 10 slowest complaint types by median resolution time:")
print(median_time_by_type.round(2))


# 7. Find complaint types that are both common and slow
complaint_count_by_type = df.groupby("complaint_type")["unique_key"].count()
avg_resolution_by_type = df.groupby("complaint_type")["resolution_time_hours"].mean()

type_summary = pd.DataFrame({
    "complaint_count": complaint_count_by_type,
    "avg_resolution_hours": avg_resolution_by_type
})

common_slow_types = type_summary[type_summary["complaint_count"] >= 100]
common_slow_types = common_slow_types.sort_values(
    "avg_resolution_hours",
    ascending=False
).head(10)

print("\nCommon complaint types with slow average resolution time:")
print(common_slow_types.round(2))


# 8. Complaint counts by month
monthly_complaints = df.groupby("created_month_name")["unique_key"].count()
monthly_complaints = monthly_complaints.sort_values(ascending=False)

print("\nComplaint counts by month:")
print(monthly_complaints)


# 9. Median resolution time by month
median_time_by_month = df.groupby("created_month_name")["resolution_time_hours"].median()
median_time_by_month = median_time_by_month.sort_values(ascending=False)

print("\nMedian resolution time by month:")
print(median_time_by_month.round(2))


# Save summary tables for later analysis and charts
type_summary.to_csv("data/processed/complaint_type_summary.csv")
avg_time_by_borough.to_csv("data/processed/avg_time_by_borough.csv")
monthly_complaints.to_csv("data/processed/monthly_complaints.csv")

print("\nSummary files saved to data/processed/")