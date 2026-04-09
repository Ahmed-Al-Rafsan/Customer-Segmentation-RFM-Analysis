USE customer_segmentation_rfm;
select * from transactions limit 10;
-- Query 5a Business question: "What are our top 10 best-selling products by total revenue?"
Select Description as Top_10_Selling_Products,round(sum(Total_Price),2) as Total_Revenue
from transactions 
group by Top_10_Selling_Products order by Total_Revenue
 desc limit 10  ;
 
 
 

