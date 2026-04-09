USE customer_segmentation_rfm;
select * from transactions limit 10;
-- Query 6 Business Question
-- "For each customer, calculate their Recency (days since last purchase), Frequency (number of orders), and Monetary (total spend)."
Select Customer_ID,
datediff((Select Max(InvoiceDate) from transactions),Max(InvoiceDate)) as Recency,
count(distinct(Invoice)) As Frequency,
round(sum(Total_Price),2) as Monetary
from transactions 
group by Customer_ID limit 20;