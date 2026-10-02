import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns 




df = pd.read_csv("online_retail.csv")



# #-------------- data view




# print(df.head())

# print(df.tail())



# print(df.shape)

# print(df.columns)

# df.info()


print(df.describe())


# # Numerical columns.

# # print(df.select_dtypes(include="number").columns)


# # # Categorical columns.

# # print(df.select_dtypes(include="object").columns)


# #-------------- CHECK DATA QUALITY


# # print(df.isnull().sum())

# # print(df.duplicated().sum())





# # a=df["Country"].unique()

# # print(a)

# # df["Country"].nunique()

# # df["Country"].value_counts()





# # ============================================================
# # CREATE USEFUL COLUMNS
# # ============================================================

# # Convert InvoiceDate from string to datetime
# df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# # Create Revenue
# df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# # Extract Year
# df["Year"] = df["InvoiceDate"].dt.year

# # Extract Month Name
# df["Month_Name"] = df["InvoiceDate"].dt.month_name()

# # Extract Day
# df["Day"] = df["InvoiceDate"].dt.day

# pd.set_option("display.max_columns", None)

# print(df.head())







