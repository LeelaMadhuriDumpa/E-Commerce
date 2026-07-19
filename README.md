MINOR PROJECT REPORT


E‑COMMERCE SALES ANALYTICS AND PRODUCT RECOMMENDATION SYSTEM USING PYTHON AND POWER BI
Submitted by


DUMPA LEELA MADHURI

In partial fulfilment of the requirements for the award of the Degree of
Bachelor of  Technology, CSE
Chaitanya Engineering College, Visakhapatnam
June, 2026

 
EXECUTIVE SUMMARY

This minor project, titled “E‑Commerce Sales Analytics and Product Recommendation System using Python and Power BI”, focuses on converting raw online transaction data into actionable business insights for an e‑commerce business. The primary objective is to analyse historical sales data, identify key revenue‑driving products and customer patterns, and generate data‑driven product recommendations using Market Basket Analysis.
A synthetic but realistic e‑commerce dataset was designed to simulate one year of transactions, including customers, products, categories, quantities, prices, and regions. The project follows a structured analytics workflow, starting from data generation and collection, data pre-processing, and exploratory data analysis (EDA), followed by Market Basket Analysis using the Apriori algorithm and preparation of outputs for dashboarding.
Using Python libraries such as pandas, NumPy, and mlxtend, the dataset was cleaned and transformed, key performance indicators (KPIs) like monthly revenue and top products were calculated, and association rules were generated to discover products frequently bought together. The final outputs—monthly revenue, product‑level revenue, and association rules—are exported to CSV and visualized in Power BI to create interactive dashboards for decision makers.
The project demonstrates how an end‑to‑end data analytics pipeline can support strategic decisions in e‑commerce, such as planning discounts, designing product bundles, and targeting cross‑sell opportunities. It also strengthened practical skills in data analysis, basic recommendation techniques, and business intelligence dashboard design, similar in depth and structure to the reference churn prediction report.
 
ACKNOWLEDGMENT

I would like to express my sincere gratitude to [Guide Name], [Designation], [Department], [College Name], for their constant guidance, valuable feedback, and encouragement throughout the completion of this minor project. Their support helped me understand practical aspects of data analytics and apply them to a realistic e‑commerce scenario.
I am also thankful to the faculty and staff of the [Department Name] for providing the necessary academic environment, resources, and laboratory facilities. Finally, I would like to thank my family and friends for their continuous motivation and support during the course of this project.
 
CHAPTER 1 – INTRODUCTION
1.1 Introduction to the Project
E‑commerce platforms generate large volumes of transaction data every day through online orders, product views, and customer interactions. This data contains valuable information about what customers buy, which products are popular, and how revenue changes over time. However, many small and medium businesses do not fully leverage this data to drive decisions.
This project focuses on using data analytics and Market Basket Analysis to understand sales patterns and design basic product recommendation logic. By analysing historical transaction data, the system aims to highlight important KPIs such as monthly revenue, top products, and frequently co‑purchased items that can be used to design cross‑sell and bundle offers.
1.2 Background of the Problem
In a competitive online retail environment, businesses must optimize product assortments, pricing, and promotions to attract and retain customers. Traditional spreadsheet‑based reporting is often limited to simple totals and does not reveal deeper relationships between products or customer buying behaviour.
Modern analytics techniques, especially association rule mining, can uncover combinations of products that are frequently purchased together. These insights support better store layout (for offline stores), recommendation widgets (for online stores), and targeted marketing campaigns. The challenge is to take raw transaction logs, clean and transform them, and apply the right algorithms to extract meaningful patterns.
1.3 Objectives of the Project
The main objectives of this project are:
To design and prepare a structured e‑commerce sales dataset containing customers, orders, and products.
To perform data cleaning and Exploratory Data Analysis (EDA) on transaction data.
To calculate key performance indicators such as total revenue, monthly sales, and top products by revenue.
To apply Market Basket Analysis using the Apriori algorithm and generate association rules.
To prepare output tables that can be imported into a business intelligence tool to build interactive dashboards for decision makers.
1.4 Scope of the Project
The scope of this project is limited to offline analysis of historical order data. The work includes data generation, pre-processing, EDA, Market Basket Analysis, and export of results for visualization. Real‑time recommendation engines, dynamic integration with a live e‑commerce website, and payment gateway or user interface development are outside the scope. The focus is on analytics and recommendation logic rather than full‑stack application development.
1.5 Organization of the Report
This report is organized into the following chapters:
Chapter 1 – Introduction
Chapter 2 – Project Overview and System Design
Chapter 3 – Dataset Description and Methodology
Chapter 4 – Implementation and Analysis
Chapter 5 – Results and Business Insights
Chapter 6 – Conclusion and Future Scope
 
CHAPTER 2 – PROJECT OVERVIEW AND SYSTEM DESIGN
2.1 Project Overview
The “E‑Commerce Sales Analytics and Product Recommendation System” project was developed to demonstrate how transaction data can be analysed to support business decisions. The key goals are to understand when and what customers buy, recognize high‑value products, and identify frequently co‑purchased items that can be used for recommendation and bundle design.
The project follows a structured analytics workflow: data generation and collection, data pre-processing, EDA, Market Basket Analysis, and exporting summary tables for dashboard creation. This end‑to‑end pipeline illustrates how raw data is transformed into business insights.
2.2 Tools and Technologies Used
Programming Language
Python
Libraries
NumPy – Numerical computations
Pandas – Data manipulation and analysis
Matplotlib / Seaborn – Data visualization (for EDA)
mlxtend – Frequent itemset mining and association rules (Apriori)
Development Environment
Jupyter Notebook / any Python IDE
Business Intelligence Tool
Microsoft Power BI Desktop (for dashboards)
2.3 System Architecture
The system architecture follows a simple analytics pipeline:
Data Generation / Collection – Synthetic e‑commerce transactions are generated to simulate orders across one year.
Data Pre-processing – Raw CSV is cleaned, data types are corrected, and a line amount is computed.
Exploratory Data Analysis – Sales trends, product performance, and customer distributions are explored.
Market Basket Analysis – Transactions are converted to a basket format and the Apriori algorithm is applied.
Export for Dashboarding – Summary tables and association rules are saved as CSV.
Dashboard Visualization – Power BI is used to create interactive charts and tables.
2.4 Workflow Diagram
You can insert a simple block diagram in your report similar to:
Transaction Data
↓
Data Pre-processing
↓
Exploratory Data Analysis
↓
Market Basket Analysis (Apriori)
↓
Export of Summary Tables
↓
Power BI Dashboard & Recommendations
2.5 Problem Statement
The problem addressed in this project is:
“To develop a data analytics workflow that can analyse e‑commerce transaction data, compute key sales KPIs, and generate product recommendation rules using Market Basket Analysis to support cross‑selling and bundle design.”
 
CHAPTER 3 – DATASET DESCRIPTION AND METHODOLOGY
3.1 Dataset Description
A synthetic e‑commerce dataset was generated to represent one year of online retail transactions. Each record corresponds to a line item in an order and contains information such as Order ID, Order Date, Customer ID, Product ID, Product Name, Category, Unit Price, Quantity, Region, Country, and Line Amount.
Key characteristics:
Time Period: Full calendar year
Number of Orders: Approximately 3000 orders
Number of Customers: Around 200 customers
Number of Products: Multiple products across categories like Electronics, Fashion, Groceries, Home & Kitchen, and Sports
Columns include:
OrderID, OrderDate, CustomerID
ProductID, ProductName, Category
UnitPrice, Quantity, LineAmount
Region, Country
3.2 Data Collection
The dataset was generated programmatically using Python to simulate realistic purchasing behaviour, such as varying quantities, dynamic prices, and diversified customers and regions. The generated transactions were stored in a CSV file which serves as the primary input to the analytics pipeline.
3.3 Exploratory Data Analysis (EDA)
EDA was performed to understand the structure and distribution of the data. The steps included:
Checking dataset shape and column names
Verifying data types and converting OrderDate to datetime
Inspecting missing values and duplicates
Generating summary statistics for monetary fields
Computing revenue by month, category, and product
Identifying top revenue‑generating products and categories
Visualizations like bar charts and line charts were used to study monthly revenue trends and category-wise performance.
3.4 Data Pre-processing
The following pre-processing steps were performed:
Cleaning any inconsistent or null values
Creating the LineAmount column as UnitPrice × Quantity
Deriving YearMonth from OrderDate for time series analysis
Ensuring categorical fields like Category and Region are correctly formatted
These steps improved the quality of the data and made it ready for both EDA and Market Basket Analysis.
3.5 Market Basket Analysis Methodology
For recommendation insights, Market Basket Analysis was applied using the Apriori algorithm:
Transaction data was reshaped into a basket format, where rows represent orders and columns represent products, with values indicating presence (1) or absence (0) of the product in that order.
The Apriori algorithm was used to find frequent itemsets that satisfy a minimum support threshold.
Association rules were generated from these frequent itemsets and evaluated with metrics such as support, confidence, and lift.
Rules with higher confidence and lift values were selected as meaningful recommendations (e.g., “If a customer buys a laptop, they also tend to buy a Mouse”).
3.6 Methodology Summary
The overall methodology consists of:
Data Generation & Loading
Data Cleaning and Transformation
Exploratory Data Analysis
Basket Creation and Frequent Itemset Mining
Association Rule Generation
Export of Summary Tables and Rules for Dashboarding
 
CHAPTER 4 – IMPLEMENTATION AND ANALYSIS
4.1 Data Generation and Loading
Synthetic data was generated using Python and saved as ecommerce_transactions.csv. This file was then loaded into a Jupyter Notebook using pandas. After loading, basic checks (head, info, describe) were performed to validate the dataset structure and values.
4.2 Exploratory Data Analysis
Key analyses included:
Monthly Revenue: A new YearMonth column was created and grouped to obtain revenue per month.
Top Products: Product‑level revenue was calculated and sorted to find top 10 products by revenue.
Category and Region Analysis: Grouping by Category and Region to understand which segments contribute most to sales.
These analyses provided an overview of the business performance over time and across product lines.
4.3 Market Basket Analysis Implementation
The steps for Market Basket Analysis were:
Grouping the transactions by OrderID and ProductName and summing quantities.
Unstacking to create an OrderID × ProductName matrix.
Converting quantities to binary (1 if the product appears in the order, 0 otherwise).
Running Apriori with a minimum support threshold to get frequent itemsets.
Generating association rules and sorting them by lift and confidence.
The results included a table of rules with antecedent products, consequent products, and their support, confidence, and lift values.
4.4 Export for Dashboarding
The following tables were exported to CSV:
Monthly Revenue – for time series charts.
Product Revenue – for ranked lists and bar charts.
Association Rules – for recommendation‑focused visuals.
These CSV files are ready to be imported into Power BI without additional processing.
4.5 Power BI Dashboard Overview
In Power BI, multiple report pages can be designed:
Sales Overview Page:
Cards for total revenue, total orders, and average order value.
Line chart for monthly revenue.
Bar charts for revenue by category and by country/region.
 
Product Performance Page:
Table or bar chart of top products by revenue and quantity.
Filters for category and time period.
 
Recommendation Insights Page:
Table of association rules (Antecedent, Consequent, Support, Confidence, Lift).
Visual of top “frequently bought together” product pairs.
 
CHAPTER 5 – RESULTS AND BUSINESS INSIGHTS
5.1 Sales Performance Results
The monthly revenue analysis shows how sales are distributed across the year, identifying peak and low‑performing periods. Top product and category analysis highlights which items generate the highest revenue and warrant more focus in marketing or inventory planning.
5.2 Recommendation Rules and Interpretation
The association rules derived from Market Basket Analysis reveal strong relationships between products. For example, certain electronics accessories may frequently co‑occur with high‑value devices, indicating natural bundle opportunities. High lift values suggest combinations that occur more often together than expected by chance, making them suitable for recommendation widgets and combo offers.
5.3 Business Insights
Key business insights include:
Identification of top‑selling products and categories that drive a major share of revenue.
Understanding seasonal or monthly patterns to plan promotions and stock levels.
Discovery of frequently co‑purchased products, which can be used to design bundles and cross‑sell strategies.
Ability to focus marketing efforts on high‑value customers and high‑margin products.
5.4 Practical Impact of the Project
The developed analytics pipeline and recommendation logic can be used as a decision‑support tool by e‑commerce managers. Instead of relying solely on intuition, they can use data‑driven insights to design offers, arrange product placement on the website, and plan promotions that increase average order value and customer satisfaction.
 
CHAPTER 6 – CONCLUSION AND FUTURE SCOPE
6.1 Conclusion
The “E‑Commerce Sales Analytics and Product Recommendation System using Python and Power BI” project successfully demonstrates an end‑to‑end analytics workflow for an e‑commerce business. Starting from synthetic transaction data, the project covers data pre-processing, exploratory analysis, Market Basket Analysis, and preparation of outputs for interactive dashboards.
The project shows that even simple association rule mining can produce useful product recommendations and cross‑sell opportunities. It also highlights the importance of structured data models and KPI tracking for understanding sales performance.
6.2 Future Scope
Potential future enhancements include:
Using real transactional data from a live e‑commerce platform.
Applying more advanced recommendation algorithms such as collaborative filtering or hybrid recommenders.
Integrating the analytics pipeline with a web application to provide real‑time recommendations.
Automating data refresh and dashboard updates using scheduled pipelines.
Incorporating customer‑level metrics like Recency, Frequency, and Monetary value (RFM) for deeper customer segmentation.
