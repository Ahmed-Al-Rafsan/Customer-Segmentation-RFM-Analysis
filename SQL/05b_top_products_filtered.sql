 -- Query 5b Business question: "What are our top 10 best-selling products by total revenue?"
Select Description as Top_10_Selling_Products,round(sum(Total_Price),2) as Total_Revenue
from transactions where Description not in ('Manual','POSTAGE')
group by Top_10_Selling_Products order by Total_Revenue
 desc limit 10  ;