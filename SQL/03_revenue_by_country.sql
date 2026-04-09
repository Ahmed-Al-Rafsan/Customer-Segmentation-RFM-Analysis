USE customer_segmentation_rfm;
show tables;
select * from transactions limit 10;
-- Query 3 Business question: "What is the total revenue per country, sorted from highest to lowest?"
Select Country,round(sum(Total_Price),2) as Total_Revenue_per_Country
from transactions
group by Country order by Total_Revenue_per_Country desc ;