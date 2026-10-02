import pandas as pd


df = pd.read_excel("online_retail.xlsx")

print("Rows and columns:", df.shape)

df.to_csv("online_retail.csv", index=False)

