USE customer_segmentation_rfm;
select * from transactions limit 10;
-- Query 4-Business question: "What's the total revenue per month? Sort it chronologically (oldest to newest)."
Select date_format(InvoiceDate,"%Y-%m") As Year_and_Month,
round(sum(Total_Price),2)As Monthly_Total_Revenue
from transactions 
group by Year_and_Month order by Year_and_Month asc;