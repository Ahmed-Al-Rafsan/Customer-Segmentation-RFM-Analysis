import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load the cleaned data
df = pd.read_csv(r"A:\Projects\Customer Segmentation & RFM Analysis\Data\online_retail_II_cleaned_data.csv")

# Step 2: Rename "Customer ID" to "Customer_ID" (no spaces for SQL)
df = df.rename(columns={"Customer ID": "Customer_ID"})

print("Data loaded:", df.shape)

# Step 3: Connect to MySQL
# Format: mysql+mysqlconnector://username:password@host/database
engine = create_engine("mysql+mysqlconnector://root:8989@localhost/customer_segmentation_rfm")

# Step 4: Upload the dataframe to MySQL as a table called "transactions"
df.to_sql("transactions", con=engine, if_exists="replace", index=False, chunksize=5000, method="multi")

print("Data uploaded to MySQL successfully!")