USE customer_segmentation_rfm;
select * from transactions limit 10;

WITH rfm AS (
    SELECT 
        Customer_ID,
        DATEDIFF((SELECT MAX(InvoiceDate) FROM transactions), MAX(InvoiceDate)) AS Recency,
        COUNT(DISTINCT Invoice) AS Frequency,
        ROUND(SUM(Total_Price), 2) AS Monetary
    FROM transactions
    GROUP BY Customer_ID
),
segmented AS (
    SELECT 
        Customer_ID,
        Monetary,
        CASE 
            WHEN Recency <= 30 AND Frequency >= 10 THEN 'Champion'
            WHEN Recency <= 90 AND Frequency >= 5 THEN 'Loyal Customer'
            WHEN Recency <= 30 AND Frequency <= 2 THEN 'New Customer'
            WHEN Recency > 180 AND Frequency >= 10 THEN 'Cant Lose Them'
            WHEN Recency > 180 AND Frequency <= 2 THEN 'Lost'
            WHEN Recency BETWEEN 90 AND 180 THEN 'At Risk'
            ELSE 'Need Attention'
        END AS Segment
    FROM rfm
)
SELECT 
    Segment,
    COUNT(*) AS Customer_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM segmented), 2) AS Percentage,
    ROUND(SUM(Monetary), 2) AS Total_Revenue
FROM segmented
GROUP BY Segment
ORDER BY Customer_Count DESC;