E-Commerce Sales & Customer Analytics

Project Overview

E-Commerce Sales & Customer Analytics is a Data Analysis project
focused on analyzing real-world e-commerce transaction data to
understand sales performance, customer behavior, product performance,
geographical performance, and purchasing trends.

The project follows a practical data analyst workflow using Python,
Pandas, NumPy, Matplotlib, Seaborn, and SQL/MySQL.

The analysis starts with data understanding and cleaning, followed by
feature engineering, KPI calculation, exploratory data analysis,
visualization, and business insight generation.

Dataset

The project uses an online retail transaction dataset containing
information such as:

Invoice Number

Stock Code

Product Description

Quantity

Invoice Date

Unit Price

Customer ID

Country

The cleaned dataset additionally contains:

Revenue

Year

Month Name

Day

The cleaned dataset used in the project contains 524,878 transaction
rows and 12 columns.

Project Objectives

The main objectives are to:

Understand the structure and quality of the transaction data.

Clean and prepare the dataset for analysis.

Remove duplicate and invalid sales transactions.

Calculate revenue from quantity and unit price.

Analyze overall sales and revenue performance.

Identify top-performing products.

Analyze customer purchasing behavior.

Identify high-value customers.

Analyze country-wise revenue and order performance.

Identify monthly and yearly sales trends.

Calculate important business KPIs.

Create meaningful data visualizations.

Extract business insights from the analysis.

Convert findings into practical business recommendations.

Technologies & Libraries

Technology / Library   Purpose

Python                 Main programming language
Pandas                 Data loading, cleaning, transformation and analysis
NumPy                  Numerical and statistical operations
Matplotlib             Data visualization
Seaborn                Statistical and business visualizations
MySQL / SQL            Structured business analysis

Data Analysis Workflow

Raw Dataset
     ↓
Data Loading
     ↓
Data Understanding
     ↓
Data Quality Checking
     ↓
Duplicate Removal
     ↓
Missing Value Handling
     ↓
Invalid Transaction Removal
     ↓
Data Transformation
     ↓
Feature Engineering
     ↓
KPI Calculation
     ↓
Business Analysis
     ↓
EDA
     ↓
Data Visualization
     ↓
Business Insights
     ↓
Business Recommendations

Data Cleaning

The project performs several data preparation steps.

Duplicate Removal

Duplicate records are removed before analysis.

Missing Values

Missing product descriptions are replaced with "Unknown".

Missing customer IDs are represented as 0 so that transactions without
customer identification can be handled separately during customer
analysis.

Removing Non-Sales Transactions

Because the project focuses on actual sales and revenue:

Quantity <= 0 transactions are removed.

UnitPrice <= 0 transactions are removed.

This ensures that revenue analysis is based on positive sales
transactions.

Feature Engineering

Several analytical features are created from the original transaction
data.

Revenue

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

Year

The year is extracted from InvoiceDate.

Month Name

The month name is extracted from InvoiceDate.

Day

The day of the month is extracted from InvoiceDate.

These features allow the project to perform time-based sales analysis.

KPI Analysis

The project calculates important e-commerce KPIs:

Total Revenue

Total Orders

Total Products Sold

Total Customers

Average Order Value

Average Product Price

For example, Average Order Value is calculated by first aggregating
revenue at invoice level and then calculating the average order revenue.

Business Questions

Sales Analysis

What is the total revenue?

How many orders were placed?

How many products were sold?

What is the average order value?

Which month generates the highest revenue?

Which year generates the highest revenue?

Product Analysis

Which products generate the highest revenue?

Which products have the highest quantity sold?

Which products should receive greater inventory attention?

Customer Analysis

How many unique customers are there?

Which customers generate the most revenue?

Who are the highest-value customers?

Country Analysis

Which country generates the highest revenue?

Which country has the highest number of orders?

Which countries are the major markets?

Time Analysis

Which month has the highest revenue?

Which month has the highest number of orders?

How does revenue change across years?

Key Analysis Performed

1. Revenue by Month

Monthly revenue is calculated to identify peak and low-performing
periods.

Finding: November generated the highest recorded monthly revenue,
approximately ₹15.4 lakh.

2. Orders by Month

Monthly order counts are calculated using unique invoice numbers.

Finding: November recorded the highest number of orders with 2,769
orders.

3. Top 10 Products by Revenue

Products are grouped by description and ranked according to total
revenue.

Finding: DOTCOM POSTAGE generated the highest revenue among the
products analyzed.

4. Top 10 Products by Quantity Sold

Products are ranked according to total quantity sold.

Finding: PAPER CRAFT, LITTLE BIRDIE recorded the highest quantity
sold among the products analyzed.

5. Top 10 Customers by Revenue

Customers are grouped by Customer ID and ranked by revenue.

Finding: Customer ID 0 appears as the highest revenue group in the
current analysis. This represents transactions where the customer ID was
missing and replaced with 0, so it should not be interpreted as a
single identified customer.

6. Revenue by Country

Revenue is aggregated by country.

Finding: The United Kingdom generated the highest revenue,
approximately ₹90.02 lakh.

7. Orders by Country

Orders are counted using unique invoice numbers for each country.

Finding: The United Kingdom recorded the highest number of orders
with 18,019 orders.

8. Revenue by Year

Revenue is aggregated by year to understand yearly performance.

Finding: Revenue increased substantially from approximately ₹8.21
lakh in 2010 to ₹98.21 lakh in 2011 in the analyzed data.

Data Visualization

The project creates visualizations using Matplotlib and Seaborn,
including:

Revenue by Month

Number of Orders by Month

Top 10 Products by Revenue

Top 10 Products by Quantity Sold

Top 10 Customers by Revenue

Top 10 Countries by Revenue

Top 10 Countries by Number of Orders

Revenue by Year

The visualizations are designed to make business patterns easier to
identify and communicate.

Business Insights

The analysis highlights several important patterns:

November is the strongest month in the analyzed sales data.

December also shows relatively strong sales performance.

Some months have substantially lower revenue and order volume,
creating opportunities for targeted campaigns.

A small group of products contributes significantly to revenue and
sales volume.

The United Kingdom is the dominant country in both revenue and order
volume.

High-value customer groups can be targeted for retention and loyalty
initiatives.

Revenue increased substantially between 2010 and 2011.

Business Recommendations

Based on the analysis:

1. Prepare for Peak Demand

Higher sales and order volumes during peak months require sufficient
inventory and operational capacity.

2. Improve Low-Performing Periods

Use targeted promotions and customer engagement strategies during
lower-performing months.

3. Protect Availability of High-Demand Products

High-volume and high-revenue products should receive appropriate
inventory planning.

4. Retain High-Value Customers

High-value customer groups can be targeted with loyalty programs and
personalized offers.

5. Focus on Major Markets

The United Kingdom contributes the largest share of analyzed revenue and
orders, so maintaining strong customer service and operational capacity
in this market is important.

6. Investigate Year-over-Year Growth

The significant increase in revenue from 2010 to 2011 should be
investigated further to identify the products, markets, and customer
behavior contributing to the growth.

Important Data-Quality Note

CustomerID values missing from the original dataset are replaced with
0. Therefore, Customer ID 0 in customer-level analysis represents
unidentified customers rather than one actual customer.

For a production-quality analysis, unidentified customers should be
handled separately when calculating individual customer rankings.

Project Structure

E-Commerce-Sales-Customer-Analytics/
│
├── online_retail.csv
├── cleaned_online_retail.csv
├── analysis.py
├── README.md
│
├── visualizations/
│   ├── REVENUE BY MONTH.png
│   ├── ORDERS BY MONTH.png
│   ├── TOP 10 PRODUCTS BY REVENUE.png
│   ├── TOP 10 PRODUCTS BY QUANTITY SOLD.png
│   ├── TOP 10 CUSTOMERS BY REVENUE.png
│   ├── TOP 10 COUNTRIES BY REVENUE.png
│   ├── TOP 10 COUNTRIES BY ORDERS.png
│   └── REVENUE BY YEAR.png
│
└── sql/
    └── SQL analysis files

Project Outcome

This project demonstrates an end-to-end Data Analysis workflow using
transactional e-commerce data.

It covers:

Data cleaning

Data transformation

Feature engineering

KPI calculation

Exploratory Data Analysis

Python-based analysis

SQL/MySQL business analysis

Data visualization

Customer analysis

Product analysis

Country analysis

Time-based analysis

Business insights

Business recommendations

The main goal is not simply to create charts, but to use data to answer
business questions and convert analytical findings into actionable
business decisions.
