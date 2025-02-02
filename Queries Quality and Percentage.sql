# Write your MySQL query statement below
WITH QueryStats AS (
    SELECT
        query_name,
        AVG(CAST(rating AS DECIMAL) / position) AS quality,
        100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) AS poor_query_percentage
    FROM Queries
    GROUP BY query_name
)
SELECT
    query_name,
    ROUND(quality, 2) AS quality,
    ROUND(poor_query_percentage, 2) AS poor_query_percentage
FROM QueryStats;
