import pandas as pd 
df=pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II.csv")
#shape
#print(df.shape)
#printing first 5 rows 
#print("First five rows:")
print(df.head(5))
#step 3 - trying to understand what data we have
#print(df.dtypes)
#step 4 -checking missing values
print("Total Null values:\n",df.isnull().sum())
# knowing basic statistics:
#print("Basic Statistics:\n",df.describe())
#need to see how many orders start with "C", C=Cancelled
#print(df[df["Invoice"].astype(str).str.startswith("C")].head(5))
#Now need to see, how many cancelled rows are there :
#print(df[df["Invoice"].astype(str).str.startswith("C")].shape[0])
