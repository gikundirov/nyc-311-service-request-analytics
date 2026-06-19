-- 01_basic_checks.sql
-- Purpose: Check that the SQLite database loaded correctly.

SELECT *
FROM nyc_311_requests
LIMIT 10;

SELECT COUNT(*) AS total_rows
FROM nyc_311_requests;

PRAGMA table_info(nyc_311_requests);

SELECT
    borough,
    COUNT(*) AS complaint_count
FROM nyc_311_requests
GROUP BY borough
ORDER BY complaint_count DESC;

SELECT
    complaint_type,
    COUNT(*) AS complaint_count
FROM nyc_311_requests
GROUP BY complaint_type
ORDER BY complaint_count DESC
LIMIT 10;