import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv")
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
#print(df.shape)
#print(df.head(10))


# Step 1: Create an "Order_Month" column showing which month each transaction happened
df["Order_Month"]=df["InvoiceDate"].dt.to_period("M")
#print(df[["InvoiceDate","Order_Month"]].head(10))

# Step 2: Find the FIRST purchase month for each customer (their cohort)
df["Cohort_Month"]=df.groupby("Customer ID")["Order_Month"].transform("min")
#print(df[["Customer ID","Order_Month","Cohort_Month"]].head(10))

# Quick check: look at customer 13085's later purchases
#print(df[df["Customer ID"] == 13085][["Order_Month", "Cohort_Month"]].tail(10)) 


# Step 3: Calculate the number of months between first purchase and this order
df["Cohort_Index"]=(df["Order_Month"]-df["Cohort_Month"]).apply(lambda x :x.n)
#print(df[["Customer ID","Order_Month","Cohort_Month","Cohort_Index"]].head(10))

# Quick check: look at customer 13085's later purchases
#print(df[df["Customer ID"] == 13085][["Order_Month", "Cohort_Month", "Cohort_Index"]].tail(10))


# Step 4: Count unique customers in each cohort, for each cohort index
cohort_table=df.groupby(["Cohort_Month", "Cohort_Index"])["Customer ID"].nunique().reset_index()

# Rename the misleading colum
cohort_table=cohort_table.rename(columns={"Customer ID":"Number_of_Customer"})
#print(cohort_table.head(10))


# Step 5: Reshape into a proper cohort table (rows=cohort, columns=month index)
cohort_pivot=cohort_table.pivot(index="Cohort_Month",columns="Cohort_Index",values="Number_of_Customer")
#print(cohort_pivot.head())

# Step 6: Convert raw counts into retention percentages
cohort_size=cohort_pivot.iloc[:,0]
retention=cohort_pivot.divide(cohort_size,axis=0)*100
#print(retention.round(1).head())


import seaborn as sns 
import matplotlib.pyplot as plt 
# Create the heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(retention, annot=True, fmt=".1f", cmap="Blues")
plt.title("Customer Retention by Cohort (%)")
plt.xlabel("Months Since First Purchase")
plt.ylabel("Cohort (First Purchase Month)")
plt.tight_layout()
plt.savefig(r"A:\Projects\Customer Segmentation & RFM Analysis\python\06.Cohort_Retention_Heatmap.png")
plt.show()



# Save the retention table for Power BI
retention.to_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\cohort_retention.csv")

print("Cohort retention table saved!")