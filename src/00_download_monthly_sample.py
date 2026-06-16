# NOTE:
# This script is paused for now because Python had an SSL certificate issue on Mac.
# We are using curl in the terminal to download monthly samples instead.

import pandas as pd
from urllib.parse import urlencode

# API endpoint for NYC 311 data
base_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"

# Output file
output_file = "data/raw/nyc_311_2024_monthly_sample.csv"

# Columns we need for the project
columns = (
    "unique_key,"
    "created_date,"
    "closed_date,"
    "agency,"
    "agency_name,"
    "complaint_type,"
    "descriptor,"
    "status,"
    "borough,"
    "incident_zip,"
    "latitude,"
    "longitude"
)

# Month start and end dates
months = [
    ("2024-01-01T00:00:00", "2024-02-01T00:00:00"),
    ("2024-02-01T00:00:00", "2024-03-01T00:00:00"),
    ("2024-03-01T00:00:00", "2024-04-01T00:00:00"),
    ("2024-04-01T00:00:00", "2024-05-01T00:00:00"),
    ("2024-05-01T00:00:00", "2024-06-01T00:00:00"),
    ("2024-06-01T00:00:00", "2024-07-01T00:00:00"),
    ("2024-07-01T00:00:00", "2024-08-01T00:00:00"),
    ("2024-08-01T00:00:00", "2024-09-01T00:00:00"),
    ("2024-09-01T00:00:00", "2024-10-01T00:00:00"),
    ("2024-10-01T00:00:00", "2024-11-01T00:00:00"),
    ("2024-11-01T00:00:00", "2024-12-01T00:00:00"),
    ("2024-12-01T00:00:00", "2025-01-01T00:00:00"),
]

all_data = []

# Download a sample from each month
for start_date, end_date in months:
    where_filter = (
        f"created_date >= '{start_date}' "
        f"AND created_date < '{end_date}' "
        f"AND status = 'Closed'"
    )

    params = {
        "$limit": 5000,
        "$select": columns,
        "$where": where_filter,
        "$order": "created_date"
    }

    url = f"{base_url}?{urlencode(params)}"

    month_df = pd.read_csv(url)
    all_data.append(month_df)

    print(f"{start_date[:7]} downloaded: {len(month_df)} rows")

# Combine all monthly samples
df = pd.concat(all_data, ignore_index=True)

# Save combined sample
df.to_csv(output_file, index=False)

print("\nMonthly sample created successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Saved to:", output_file)