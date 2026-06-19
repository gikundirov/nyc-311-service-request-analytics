import pandas as pd
from urllib.parse import urlencode

# NOTE:
# This script shows the planned Python download method for NYC 311 data.
# On my local Mac setup, I used curl in the terminal instead because of an SSL certificate issue.

# NYC Open Data API endpoint for 311 service requests
base_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"

# Output file for the combined monthly sample
output_file = "data/raw/nyc_311_2024_monthly_sample.csv"

# Columns selected for this project
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

# Date ranges used to collect a small sample from each month of 2024
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

# Download up to 5,000 closed complaints from each month
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


# Combine all monthly samples into one DataFrame
df = pd.concat(all_data, ignore_index=True)

# Save the final combined sample
df.to_csv(output_file, index=False)

print("\nMonthly sample created successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Saved to:", output_file)