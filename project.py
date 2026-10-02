import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# import mysql.connector


df = pd.read_csv("online_retail.csv")


# ---------------/duplicate values
# print(df.duplicated().sum())

df=df.drop_duplicates()

# print(df.duplicated().sum()) # for checkingduplicates drop succesfully



# -------------null values

# print(df.isnull().sum())

# # Fill missing values
df["Description"] = df["Description"].fillna("Unknown")
df["CustomerID"] = df["CustomerID"].fillna(0)

# Check again
# print(df.isnull().sum().sum())



# ============================================================
# REMOVE NON-SALES TRANSACTIONS
# ============================================================

# Since this project focuses on actual sales and revenue,
# transactions with zero or negative quantity/price are
# excluded from the sales analysis.
#
# Quantity <= 0:
#     Does not represent a positive sale.
#
# UnitPrice <= 0:
#     Does not contribute positive sales revenue.


# print(df[df["Quantity"] < 0])


# ----------------------before removing
# print((df["Quantity"] <= 0).sum())
# print((df["UnitPrice"] <= 0).sum())

# print(df.shape)


# ----------------------- removing
df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()



# ----------------------------after removing
# print(df.shape)
# print((df["Quantity"] <= 0).sum())
# print((df["UnitPrice"] <= 0).sum())



# Convert InvoiceDate
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Create Year
df["Year"] = df["InvoiceDate"].dt.year

# Create Month Name
df["Month_Name"] = df["InvoiceDate"].dt.month_name()

# Create Day
df["Day"] = df["InvoiceDate"].dt.day

# Save cleaned dataset
df.to_csv("cleaned_online_retail.csv", index=False)


# # Display after creating columns
# pd.set_option("display.max_columns", None)

# print(df.head())





# ============================================================
# STEP : KPI CALCULATION
# ============================================================

# Total Revenue
total_revenue = df["Revenue"].sum()


# Total Orders
total_orders = df["InvoiceNo"].nunique()


# Total Products Sold
total_products_sold = df["Quantity"].sum()


# Total Customers
total_customers = df.loc[
    df["CustomerID"] != 0,
    "CustomerID"
].nunique()


# Average Order Value
average_order_value = (
    df.groupby("InvoiceNo")["Revenue"]
      .sum()
      .mean()
)


# Average Product Price
average_product_price = df["UnitPrice"].mean()


# Display KPIs
# print("========== E-COMMERCE KPIs ==========")
# print("Total Revenue:", total_revenue)
# print("Total Orders:", total_orders)
# print("Total Products Sold:", total_products_sold)
# print("Total Customers:", total_customers)
# print("Average Order Value:", average_order_value)
# print("Average Product Price:", average_product_price)



# ============================================================
#  BUSINESS QUESTIONS
# ============================================================


# 1]. Highest revenue in which month

monthly_revenue = (
    df.groupby("Month_Name")["Revenue"]
      .sum()
)

# print(monthly_revenue)

# Ans:  November     1503866.780


# 2]. Highest number of orders in which month

monthly_orders = (
    df.groupby("Month_Name")["InvoiceNo"]
      .nunique()
)

# print(monthly_orders)

# Ans:  November     2769


# 3]. Top 10 products by revenue

product_revenue = (
    df.groupby("Description")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# print(product_revenue)




# 4]. Top 10 products by quantity sold

product_quantity = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# print(product_quantity)



# 5]. Top 10 customers by revenue

customer_revenue = (
    df.groupby("CustomerID")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# print(customer_revenue)



# 6]. Country with highest revenue

country_revenue = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

# print(country_revenue)

# Ans:  United Kingdom          9001744.094


# 7]. Country with highest number of orders

country_orders = (
    df.groupby("Country")["InvoiceNo"]
      .nunique()
      .sort_values(ascending=False)
)

# print(country_orders)

# Ans:   United Kingdom          18019


# 8]. Revenue by year

yearly_revenue = (
    df.groupby("Year")["Revenue"]
      .sum()
)

# print(yearly_revenue)




# ============================================================
#  DATA VISUALIZATION
# ============================================================


# ============================================================
# STEP 11 : DATA VISUALIZATION
# ============================================================


# ============================================================
# 1]. REVENUE BY MONTH
# ============================================================

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=monthly_revenue.index,
    y=monthly_revenue.values / 100000,
    palette="viridis"
)

plt.title(
    "Revenue by Month",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Revenue (Lakh)")

plt.xticks(rotation=45)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f L",
        padding=3
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig(' REVENUE BY MONTH.png')

plt.show()




# Business Insight — Revenue by Month

# November generated the highest revenue of approximately ₹15.4 lakh, followed by December with approximately ₹14.59 lakh. During these peak months, the business should ensure sufficient inventory and maintain efficient workflow to handle the higher demand.

# February to May recorded relatively low revenue, with an average of approximately ₹6.5 lakh. These low-performing months provide an opportunity to improve sales through promotions, customer engagement, and better preparation for the upcoming peak season.

# ============================================================
# 2]. ORDERS BY MONTH
# ============================================================

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=monthly_orders.index,
    y=monthly_orders.values,
    palette="coolwarm"
)

plt.title(
    "Number of Orders by Month",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

for container in ax.containers:
    ax.bar_label(
        container,
        padding=3
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('ORDERS BY MONTH.png')

plt.show()


# Business Insight — Orders by Month

# November recorded the highest number of orders with 2,769 orders, followed by December with 2,378 orders. These peak months indicate higher customer demand, so the business should ensure sufficient inventory and operational capacity.

# January and February recorded the lowest order volumes, averaging approximately 1,150 orders. The medium-performing months recorded around 1,500 orders on average, providing an opportunity to improve sales through targeted promotions and customer engagement before the peak season.


# # ============================================================
# # 3]. TOP 10 PRODUCTS BY REVENUE
# # ============================================================

plt.figure(figsize=(12, 7))

ax = sns.barplot(
    x=product_revenue.head(10).values / 100000,
    y=product_revenue.head(10).index,
    palette="magma"
)

plt.title(
    "Top 10 Products by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (Lakh)")
plt.ylabel("Product")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f L",
        padding=3
    )

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('TOP 10 PRODUCTS BY REVENUE.png')

plt.show()



# Business Insight — Top 10 Products by Revenue

# DOTCOM POSTAGE generated the highest revenue of ₹2.06 lakh, followed by REGENCY CAKESTAND 3 TIER at ₹1.74 lakh and PAPER CRAFT, LITTLE BIRDIE at ₹1.68 lakh. These products should be prioritized for stock availability and marketing.


# # ============================================================
# # 4]. TOP 10 PRODUCTS BY QUANTITY SOLD
# # ============================================================

plt.figure(figsize=(12, 7))

ax = sns.barplot(
    x=product_quantity.head(10).values,
    y=product_quantity.head(10).index,
    palette="crest"
)

plt.title(
    "Top 10 Products by Quantity Sold",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Quantity Sold")
plt.ylabel("Product")

for container in ax.containers:
    ax.bar_label(
        container,
        padding=3
    )

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('TOP 10 PRODUCTS BY QUANTITY SOLD.png')

plt.show()



# Business Insight — Top 10 Products by Quantity Sold

# PAPER CRAFT, LITTLE BIRDIE had the highest quantity sold with 80,995 units, followed by MEDIUM CERAMIC TOP STORAGE JAR with 78,033 units. These high-demand products should be kept well-stocked to avoid stock shortages and maintain sales.


# # ============================================================
# # 5]. TOP 10 CUSTOMERS BY REVENUE
# # ============================================================

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=customer_revenue.head(10).values / 100000,
    y=customer_revenue.head(10).index.astype(str),
    palette="rocket"
)

plt.title(
    "Top 10 Customers by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (Lakh)")
plt.ylabel("Customer ID")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f L",
        padding=3
    )

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('TOP 10 CUSTOMERS BY REVENUE.png')

plt.show()


# Business Insight — Top 10 Customers by Revenue

# Customer 0 generated the highest revenue of ₹17.55 lakh, followed by Customer 14646 with ₹2.80 lakh and Customer 18102 with ₹2.60 lakh. The business should focus on retaining high-value customers through loyalty benefits and personalized offers.


# # ============================================================
# # 6]. TOP 10 COUNTRIES BY REVENUE
# # ============================================================

top_country_revenue = country_revenue.head(10)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=top_country_revenue.values / 100000,
    y=top_country_revenue.index,
    palette="Spectral"
)

plt.title(
    "Top 10 Countries by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (Lakh)")
plt.ylabel("Country")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f L",
        padding=3
    )

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('TOP 10 COUNTRIES BY REVENUE.png')

plt.show()

# Business Insight — Top 10 Countries by Revenue

# The United Kingdom generated the highest revenue of ₹90.02 lakh, significantly higher than the Netherlands (₹2.85 lakh) and EIRE (₹2.83 lakh). This indicates that the UK is the most important market, so the business should prioritize inventory, marketing, and customer retention in this market.


# # ============================================================
# # 7]. TOP 10 COUNTRIES BY ORDERS
# # ============================================================

top_country_orders = country_orders.head(10)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    x=top_country_orders.values,
    y=top_country_orders.index,
    palette="cubehelix"
)

plt.title(
    "Top 10 Countries by Number of Orders",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Number of Orders")
plt.ylabel("Country")

for container in ax.containers:
    ax.bar_label(
        container,
        padding=3
    )

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.savefig('TOP 10 COUNTRIES BY ORDERS.png')

plt.show()


# # Business Insight — Top 10 Countries by Number of Orders

# # The United Kingdom recorded the highest number of orders with 18,019 orders, while Germany and France followed with 457 and 392 orders respectively. The business should focus on maintaining strong customer engagement and operational capacity in the UK market.

# # ============================================================
# # 8]. REVENUE BY YEAR
# # ============================================================

plt.figure(figsize=(8, 6))

ax = sns.barplot(
    x=yearly_revenue.index,
    y=yearly_revenue.values / 100000,
    palette="Set2"
)

plt.title(
    "Revenue by Year",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Year")
plt.ylabel("Revenue (Lakh)")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f L",
        padding=3
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)


plt.tight_layout()
plt.savefig('REVENUE BY YEAR.png')
plt.show()


# Business Insight — Revenue by Year

# Revenue increased significantly from ₹8.21 lakh in 2010 to ₹98.21 lakh in 2011, showing strong business growth. The business should analyze the factors behind this growth and continue investing in the strategies and markets contributing to higher revenue.
