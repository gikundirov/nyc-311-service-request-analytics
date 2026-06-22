import os
import pandas as pd
import matplotlib.pyplot as plt

# File paths
cleaned_file = "data/processed/nyc_311_2024_cleaned.csv"
chart_folder = "dashboard"

# Make sure the dashboard folder exists before saving charts
os.makedirs(chart_folder, exist_ok=True)

# Load cleaned data
df = pd.read_csv(cleaned_file)

print("Cleaned data loaded.")
print("Rows and columns:", df.shape)


def add_bar_labels():
    """Add number labels to the bars in a bar chart."""
    ax = plt.gca()

    for bar in ax.patches:
        value = bar.get_height()

        if value > 0:
            ax.annotate(
                f"{value:,.0f}",
                (bar.get_x() + bar.get_width() / 2, value),
                ha="center",
                va="bottom",
                fontsize=8
            )


def add_horizontal_bar_labels():
    """Add number labels to horizontal bar charts."""
    ax = plt.gca()

    for bar in ax.patches:
        value = bar.get_width()

        if value > 0:
            ax.annotate(
                f"{value:,.0f}",
                (value, bar.get_y() + bar.get_height() / 2),
                ha="left",
                va="center",
                fontsize=8
            )


# Chart 1: complaints by borough
complaints_by_borough = df["borough"].value_counts()

plt.figure(figsize=(8, 5))
complaints_by_borough.plot(kind="bar")
plt.title("Complaints by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.3)
add_bar_labels()
plt.tight_layout()
plt.savefig(f"{chart_folder}/complaints_by_borough.png", dpi=300)
plt.close()


# Chart 2: top 10 complaint types
top_complaints = df["complaint_type"].value_counts().head(10)
top_complaints = top_complaints.sort_values()

plt.figure(figsize=(10, 6))
top_complaints.plot(kind="barh")
plt.title("Top 10 Complaint Types")
plt.xlabel("Number of Complaints")
plt.ylabel("Complaint Type")
plt.grid(axis="x", linestyle="--", alpha=0.3)
add_horizontal_bar_labels()
plt.tight_layout()
plt.savefig(f"{chart_folder}/top_10_complaints.png", dpi=300)
plt.close()


# Chart 3: average resolution time by borough
avg_time_by_borough = df.groupby("borough")["resolution_time_days"].mean()
avg_time_by_borough = avg_time_by_borough.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
avg_time_by_borough.plot(kind="bar")
plt.title("Average Resolution Time by Borough")
plt.xlabel("Borough")
plt.ylabel("Average Resolution Time (Days)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.3)
add_bar_labels()
plt.tight_layout()
plt.savefig(f"{chart_folder}/avg_resolution_by_borough.png", dpi=300)
plt.close()


# Month labels for the two monthly charts
month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]


# Chart 4: monthly complaint volume
monthly_complaints = df.groupby("created_month")["unique_key"].count()
monthly_complaints = monthly_complaints.reindex(range(1, 13))

plt.figure(figsize=(8, 5))
monthly_complaints.plot(kind="line", marker="o")
plt.title("Monthly Complaint Volume")
plt.xlabel("Month")
plt.ylabel("Number of Complaints")
plt.xticks(range(1, 13), month_names)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{chart_folder}/monthly_complaints.png", dpi=300)
plt.close()


# Chart 5: monthly average resolution time
monthly_avg_time = df.groupby("created_month")["resolution_time_days"].mean()
monthly_avg_time = monthly_avg_time.reindex(range(1, 13))

plt.figure(figsize=(8, 5))
monthly_avg_time.plot(kind="line", marker="o")
plt.title("Monthly Average Resolution Time")
plt.xlabel("Month")
plt.ylabel("Average Resolution Time (Days)")
plt.xticks(range(1, 13), month_names)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{chart_folder}/monthly_resolution_time.png", dpi=300)
plt.close()


# Chart 6: slowest common complaint types
complaint_counts = df.groupby("complaint_type")["unique_key"].count()
complaint_avg_time = df.groupby("complaint_type")["resolution_time_days"].mean()

complaint_summary = pd.DataFrame({
    "complaint_count": complaint_counts,
    "avg_resolution_days": complaint_avg_time
})

common_complaints = complaint_summary[complaint_summary["complaint_count"] >= 100]
slowest_common_complaints = common_complaints.sort_values(
    "avg_resolution_days",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
slowest_common_complaints["avg_resolution_days"].sort_values().plot(kind="barh")
plt.title("Slowest Common Complaint Types")
plt.xlabel("Average Resolution Time (Days)")
plt.ylabel("Complaint Type")
plt.grid(axis="x", linestyle="--", alpha=0.3)
add_horizontal_bar_labels()
plt.tight_layout()
plt.savefig(f"{chart_folder}/slowest_common_complaints.png", dpi=300)
plt.close()


# Chart 7: agency workload
top_agencies = df["agency"].value_counts().head(10)

plt.figure(figsize=(8, 5))
top_agencies.plot(kind="bar")
plt.title("Top Agencies by Complaint Volume")
plt.xlabel("Agency")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.3)
add_bar_labels()
plt.tight_layout()
plt.savefig(f"{chart_folder}/agency_workload.png", dpi=300)
plt.close()


print("Charts created successfully.")
print("Charts saved in the dashboard folder.")