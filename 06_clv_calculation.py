import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\rfm_table.csv")
pd.set_option('display.float_format','{:,.2f}'.format)
#print(df.shape)
#print(df.head(10))

# Step 1: Calculate Average Order Value for each customer
df["AOV"]=df["Monetary"]/df["Frequency"]
#print(df[["Customer ID","Monetary","Frequency","AOV"]].head(10))


# Step 2: Calculate real lifespan from the cleaned transaction data
# Load the original cleaned data which has all the dates
transactions = pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv")
transactions["InvoiceDate"]=pd.to_datetime(transactions["InvoiceDate"])


# For each customer, find their first and last purchase date
first_purchase =transactions.groupby("Customer ID")["InvoiceDate"].min()
last_purchase=transactions.groupby("Customer ID")["InvoiceDate"].max()

# Calculate lifespan in days, then convert to months
lifespan_days =(last_purchase-first_purchase).dt.days
lifespan_months=lifespan_days/30

# Add it back to our RFM table by merging on Customer ID
df=df.merge(lifespan_months.rename("Lifespan_Months"),on="Customer ID")

# Make sure no customer has 0 months (replace zeros with 1)
df["Lifespan_Months"]=df["Lifespan_Months"].clip(lower=1)
#print(df[["Customer ID","Lifespan_Months"]].head(10))

# Step 3: Calculate Customer Lifetime Value
df["CLV"]=df["AOV"]*df["Frequency"]*df["Lifespan_Months"]

#print(df[["Customer ID","AOV","Frequency","Lifespan_Months","CLV"]].head(10))


# Step 4: Calculate average CLV per segment
clv_by_segment=df.groupby("Segments")["CLV"].mean().sort_values(ascending=False)
#print("Average CLV by Segment:")
#print(clv_by_segment)

# Step 5: Calculate total revenue at risk from "Can't Lose Them" segment
at_risk=df[df["Segments"] == "Can't Lose Them"]
revenue_at_risk =at_risk["CLV"].sum()
customer_count=len(at_risk)
#print(f"Customers at risk: {customer_count}")
#print(f"Total revenue at risk: £{revenue_at_risk:,.2f}")

df.to_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\customer_clv.csv", index=False)
print("Saved Successfully")