# E-Commerce Sales & Customer Analytics

## 1. Project Overview

This project is a **Data Analysis / Data Analytics project** focused on
real-world e-commerce transaction data.

The objective is to understand:

-   Sales performance
-   Revenue trends
-   Customer purchasing behavior
-   Product performance
-   Country-wise performance
-   Time-based purchasing trends

The project follows a practical Data Analyst workflow using Python and
its data-analysis libraries, together with SQL/MySQL for structured
business analysis.

------------------------------------------------------------------------

## 2. Dataset

The project uses online retail transaction data containing fields such
as:

-   `InvoiceNo`
-   `StockCode`
-   `Description`
-   `Quantity`
-   `InvoiceDate`
-   `UnitPrice`
-   `CustomerID`
-   `Country`

After cleaning and feature engineering, the dataset contains:

-   `Revenue`
-   `Year`
-   `Month_Name`
-   `Day`

The supplied cleaned dataset contains **524,878 rows and 12 columns**.

------------------------------------------------------------------------

## 3. Technologies Used

### Python

Python is used as the primary language for data preparation, analysis,
KPI calculation and visualization.

### Pandas

Used for:

-   Reading CSV data
-   Removing duplicates
-   Handling missing values
-   Filtering transactions
-   Grouping data
-   Aggregation
-   Feature creation
-   Exporting the cleaned dataset

### NumPy

Used as part of the numerical analysis environment.

### Matplotlib

Used for plotting and visualization.

### Seaborn

Used to create business-oriented statistical charts and bar plots.

### SQL / MySQL

SQL/MySQL is part of the project's analytical scope for structured
business analysis. The supplied Python file, however, currently contains
the MySQL connector import as commented code, so the exact SQL queries
should be documented from the separate SQL work rather than inferred
from this Python file.

------------------------------------------------------------------------

## 4. Data Cleaning

### 4.1 Duplicate Values

Duplicate rows are removed using Pandas.

``` python
df = df.drop_duplicates()
```

### 4.2 Missing Product Descriptions

Missing descriptions are replaced with:

``` text
Unknown
```

### 4.3 Missing Customer IDs

Missing Customer IDs are replaced with `0`.

This allows unidentified transactions to remain in sales analysis while
they can be distinguished from identified customers.

### 4.4 Removing Invalid Sales Transactions

Transactions with:

``` text
Quantity <= 0
```

or

``` text
UnitPrice <= 0
```

are removed because the project focuses on positive sales and revenue.

------------------------------------------------------------------------

## 5. Feature Engineering

### Revenue

Revenue is calculated as:

``` text
Revenue = Quantity × UnitPrice
```

### Year

The year is extracted from the invoice date.

### Month Name

The month name is extracted from the invoice date.

### Day

The day of the month is extracted from the invoice date.

These features allow the analysis to investigate sales performance over
time.

------------------------------------------------------------------------

## 6. KPI Analysis

The project calculates:

### Total Revenue

Sum of transaction-level revenue.

### Total Orders

Number of unique invoice numbers.

### Total Products Sold

Sum of quantity sold.

### Total Customers

Number of unique non-zero Customer IDs.

### Average Order Value

Revenue is first aggregated by invoice and then averaged.

### Average Product Price

Mean of `UnitPrice`.

------------------------------------------------------------------------

## 7. Business Analysis

### 7.1 Revenue by Month

Monthly revenue is calculated using:

``` text
Month_Name → Revenue → Sum
```

November recorded the highest monthly revenue at approximately **₹15.4
lakh**.

December followed with approximately **₹14.59 lakh**.

------------------------------------------------------------------------

### 7.2 Orders by Month

Monthly orders are calculated using unique invoice numbers.

November recorded the highest number of orders with **2,769 orders**.

------------------------------------------------------------------------

### 7.3 Top 10 Products by Revenue

Products are grouped by `Description`, their revenue is summed, sorted
in descending order, and the top 10 are selected.

`DOTCOM POSTAGE` generated the highest revenue in the current analysis
at approximately **₹2.06 lakh**.

------------------------------------------------------------------------

### 7.4 Top 10 Products by Quantity Sold

Products are grouped by description and ranked according to total
quantity sold.

`PAPER CRAFT, LITTLE BIRDIE` recorded the highest quantity sold in the
current analysis.

------------------------------------------------------------------------

### 7.5 Top 10 Customers by Revenue

Customers are grouped using `CustomerID` and ranked according to
revenue.

A data-quality limitation exists here: Customer ID `0` represents
transactions whose original Customer ID was missing. Therefore, it
should not be interpreted as one individual customer.

------------------------------------------------------------------------

### 7.6 Revenue by Country

Revenue is aggregated by country.

The **United Kingdom** generated the highest revenue at approximately
**₹90.02 lakh**.

------------------------------------------------------------------------

### 7.7 Orders by Country

Orders are calculated using unique invoice numbers by country.

The **United Kingdom** recorded the highest number of orders with
**18,019 orders**.

------------------------------------------------------------------------

### 7.8 Revenue by Year

Revenue is grouped by year.

The analyzed data shows revenue increasing from approximately **₹8.21
lakh in 2010** to approximately **₹98.21 lakh in 2011**.

------------------------------------------------------------------------

## 8. Data Visualization

The project generates the following visualizations:

1.  Revenue by Month
2.  Number of Orders by Month
3.  Top 10 Products by Revenue
4.  Top 10 Products by Quantity Sold
5.  Top 10 Customers by Revenue
6.  Top 10 Countries by Revenue
7.  Top 10 Countries by Number of Orders
8.  Revenue by Year

Charts are created using **Seaborn and Matplotlib**.

------------------------------------------------------------------------

## 9. Business Insights

### Peak Sales Period

November has the highest revenue and order volume, indicating a strong
peak period.

### Product Performance

A small group of products contributes strongly to revenue and quantity
sold.

### Customer Value

The analysis identifies high-revenue customer groups that can be
considered for retention and loyalty strategies.

### Geographic Performance

The United Kingdom is the dominant market in the current analysis based
on both revenue and order volume.

### Yearly Growth

Revenue increased significantly from 2010 to 2011 in the analyzed
dataset.

### Low-Performing Periods

Several months show substantially lower revenue and order volume than
the peak period, suggesting an opportunity for targeted promotional
activity.

------------------------------------------------------------------------

## 10. Business Recommendations

### Inventory Planning

Maintain sufficient inventory and operational capacity before
high-demand periods.

### Product Stocking

Prioritize availability of products that generate high revenue or high
sales volume.

### Customer Retention

Use loyalty initiatives and personalized offers for high-value
customers.

### Market Focus

Maintain strong operational and customer-service capabilities in the
United Kingdom market.

### Seasonal Marketing

Use targeted promotions and customer engagement strategies during weaker
sales periods.

### Growth Investigation

Analyze the factors behind the large increase in revenue between 2010
and 2011.

------------------------------------------------------------------------

## 11. Project Workflow

``` text
Business Problem
      ↓
Dataset Understanding
      ↓
Data Loading
      ↓
Data Quality Checking
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Feature Engineering
      ↓
KPI Calculation
      ↓
SQL / MySQL Business Analysis
      ↓
Python / Pandas Analysis
      ↓
EDA
      ↓
Data Visualization
      ↓
Business Insights
      ↓
Business Recommendations
      ↓
Conclusion
```

------------------------------------------------------------------------

## 12. Project Outcome

The project demonstrates how raw transactional data can be converted
into useful business information through a structured Data Analysis
workflow.

The final analysis covers:

-   Data cleaning
-   Data transformation
-   Feature engineering
-   KPI calculation
-   EDA
-   Python analysis
-   SQL/MySQL analysis
-   Visualization
-   Sales analysis
-   Customer analysis
-   Product analysis
-   Country analysis
-   Time-based analysis
-   Business insights
-   Business recommendations

------------------------------------------------------------------------

## 13. Conclusion

The project demonstrates an end-to-end Data Analysis approach to
e-commerce transaction data.

Python and its analytical libraries are used to prepare, transform,
analyze and visualize the data, while SQL/MySQL forms part of the
structured business-analysis workflow.

The analysis identifies important patterns in revenue, orders, products,
customers, countries and time periods and converts those patterns into
practical business questions and recommendations.
