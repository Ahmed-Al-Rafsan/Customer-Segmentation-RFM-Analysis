USE customer_segmentation_rfm;
select * from transactions limit 10;
-- Query 7: "For each customer, calculate their RFM values, 
-- then assign them a segment label (Champion, Loyal Customer, 
-- At Risk, Lost, etc.) based on their buying behaviour. Show the first 20 results."
WITH rfm AS (
    SELECT 
        Customer_ID,
        DATEDIFF((SELECT MAX(InvoiceDate) FROM transactions), MAX(InvoiceDate)) AS Recency,
        COUNT(DISTINCT Invoice) AS Frequency,
        ROUND(SUM(Total_Price), 2) AS Monetary
    FROM transactions
    GROUP BY Customer_ID
)
SELECT 
    Customer_ID,
    Recency,
    Frequency,
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
LIMIT 20;