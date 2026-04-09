import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv")
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])


# Setting the reference date (one day after the last transaction in the data)
reference_date=df["InvoiceDate"].max()+pd.Timedelta(days=1)
#print(f"Last Transaction Date :{df["InvoiceDate"].max()}")
#print("Reference_Date :",reference_date)


# Calculate RFM values for each customer
last_purchase=df.groupby("Customer ID")["InvoiceDate"].max()
last_purchase=(reference_date-last_purchase).dt.days
#print(last_purchase.head(10))


# Frequency: How many separate orders each customer made
frequency=df.groupby("Customer ID")["Invoice"].nunique()
#print(frequency.head(10))


# Monetary: How much total each customer spent
monetary=df.groupby('Customer ID')["Total_Price"].sum()
#print(monetary.head(10))


# Combine R, F, M into one table
rfm=pd.DataFrame({
    "Recency":last_purchase,
    "Frequency":frequency,
    "Monetary":monetary
})
#print(rfm.head(10))


# Score Recency: 5 = most recent, 1 = least recent
rfm["R-Score"]=pd.qcut(rfm["Recency"],q=5,labels=[5,4,3,2,1])
# Score Frequency: 5 = most frequent, 1 = least frequent
rfm["F-Score"]=pd.qcut(rfm["Frequency"].rank(method="first"),q=5,labels=[1,2,3,4,5])
# Score Monetary: 5 = most frequent, 1 = least frequent
rfm["M-Score"]=pd.qcut(rfm['Monetary'],q=5,labels=[1,2,3,4,5])

#print(rfm.head(10))


# Combine R, F, M scores into one string (e.g., "555" = best customer)
rfm["RFM_Score"]=rfm["R-Score"].astype(str)+rfm["F-Score"].astype(str)+rfm["M-Score"].astype(str)

#print(rfm[["R-Score","F-Score","M-Score","RFM_Score"]].head(10))


# Assign customer segments based on R and F scores
segment=[]
for i in range (len(rfm)):
    r=int(rfm["R-Score"].iloc[i])
    f=int(rfm["F-Score"].iloc[i])
    if r >=4 and f >=4:
        segment.append("Champion")
    elif  r >=4 and f <=2:
        segment.append("New Customer")
    elif  r >=2 and f >=4:
        segment.append("Can't Lose Them")
    elif  r <=2 and f <=2:
        segment.append("Lost")
    elif  r ==3 and f ==3:
        segment.append("Promising")
    elif  r >=3 and f <=2:
        segment.append("Need Attention")
    else:
        segment.append("Loyal Customer")
rfm["Segments"]=segment
#print(rfm["Segments"].value_counts())


# Save the RFM table for future use
rfm.to_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\rfm_table.csv")

print("RFM table saved!")