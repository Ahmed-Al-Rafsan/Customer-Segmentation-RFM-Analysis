import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II.csv")
#step_1
#print("Before Data Cleaning:\n",df.shape)
df=df.dropna(subset=["Customer ID"])
#print("After deleting the empty Customer_ID Column:\n",
      #"now we have",df.shape[0],"rows")
#step_2 
#removing the cancelled rows 
df=df[~df["Invoice"].astype(str).str.startswith("C")]
#print("After deleting the cancelled Invoices:\n")
#print('rows:',df.shape[0],"\ncolumns:",df.shape[1])
df=df[df["Quantity" ]>0]
#checking after removing negetives
#print("rows",df.shape[0])
df=df[df["Price" ]>0]
#now converting InvoiceDate to proper Date from text 
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
#changing the Customer ID 
df["Customer ID"]=df["Customer ID"].astype(int)
df["Total_Price"]=df["Price"]*df["Quantity"]
print('Total_Price:',df["Total_Price"].head(10))
df.to_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv",index=False)
print("CSV saved successfully")
print(df.shape)