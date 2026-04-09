USE customer_segmentation_rfm;
Select * from transactions limit 10;
-- Query 1.1: Count total transactions
Select count(*) as Total_Transactions from transactions ;

-- Query 1.2: Count unique customers
Select count(distinct(Customer_ID)) as Unique_Customer_In_Total from transactions ;

-- Query 1.3: Date range of the data
Select Min(InvoiceDate) As First_Order_Date from transactions;
Select Max(InvoiceDate) As Last_Order_Date from transactions;


Select * from transactions limit 10;
-- Query 2: Top 10 Customers by Total Spend
Select Customer_ID as Top_10_Customers ,Round(Sum(Total_Price),2) As Total_Revenue
from transactions 
group by Customer_ID order by Sum(Total_Price) desc limit 10  ;