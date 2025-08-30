# Global_superstore_analysis

Project Overview

The Global Superstore Project analyzes sales, profit, and customer insights using Python (Pandas, Matplotlib/Seaborn) for data cleaning & visualization, MySQL for database management
The goal of this project is to extract meaningful business insights that help in decision-making regarding sales, customers, and shipping efficiency.

🗂 Dataset

Source: Global Superstore Dataset (public Kaggle dataset)

Size: ~50,000 rows

Features:

Order Details (Order ID, Date, Ship Mode)

Customer Details (ID, Name, Segment, Region, Country)

Product Details (Product ID, Category, Sub-Category, Sales, Profit)

Shipping Details (Shipping Cost, Ship Date, Delivery Time)

🔑 Key Steps
1️⃣ Data Cleaning (Python - Pandas)

Removed missing & duplicate values

Converted date columns into datetime format

Created new calculated columns:

Profit Margin

Shipping Days

Year, Month, Week

2️⃣ Exploratory Data Analysis (Matplotlib/Seaborn)

Top 10 products

Sales Distribution by category

monthly_sals

3️⃣ Database Management (MySQL)

Created SQL tables for the dataset

Performed advanced queries for insights, e.g.:

Cohort analysis

RFM Analysis

TOP 5 Products per regiony

etc
