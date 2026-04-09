import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv")
pd.set_option('display.float_format','{:,.2f}'.format)

# EDA Question 1: What is the total revenue?
total_revenue=df["Total_Price"].sum()
#print(f'Total Revenue:£ {total_revenue:,.2f}')


# EDA Question 2: How many unique customers?
Unique_Customer=df["Customer ID"].nunique()
#print(f'Number Of Customer={Unique_Customer:,}')


# EDA Question 3: Top 10 countries by revenue
top_countries=df.groupby("Country")["Total_Price"].sum().sort_values(ascending=False).head(10)
#print(f'Top 10 Country :\n{top_countries}')


# EDA Question 4: Top 10 products by revenue
top_products=df.groupby("Description")["Total_Price"].sum().sort_values(ascending=False).head(10)
#print(f"Top 10 Products:\n{top_products}")


# EDA Question 5: Monthly revenue trend
import matplotlib.pyplot as plt 
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
df["Month"]=df["InvoiceDate"].dt.to_period("M")

monthly_revenue=df.groupby("Month")["Total_Price"].sum()
plt.figure(figsize=(12,5))
plt.plot(monthly_revenue.index.astype(str),monthly_revenue.values)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"A:\Projects\Customer Segmentation & RFM Analysis\python\04.Monthly_Revenue.png")
plt.show()



# EDA Question 6: Top 10 countries bar chart (excluding UK to see others clearly)
top_10_countries_without_UK=df[df["Country"]!="United Kingdom"].groupby("Country")["Total_Price"].sum().sort_values(ascending=False).head(10)
#print(top_10_countries_without_UK)
plt.figure(figsize=(10,5))
plt.bar(top_10_countries_without_UK.index,top_10_countries_without_UK.values)
plt.title("Top 10 Countries by Revenue (Excluding UK)")
plt.xlabel("Country")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"A:\Projects\Customer Segmentation & RFM Analysis\python\05.Top 10 Countries by Revenue(Excluding UK).png")
plt.show()