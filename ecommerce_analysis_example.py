import pandas as pd
from datetime import datetime

# Load data
orders = pd.read_csv("ecommerce_transactions.csv")
orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])

# Basic EDA
print("Rows, Columns:", orders.shape)
print("\nColumns:", orders.columns.tolist())

# Monthly revenue
orders['YearMonth'] = orders['OrderDate'].dt.to_period('M').astype(str)
monthly_rev = orders.groupby('YearMonth')['LineAmount'].sum().reset_index()
print("\nMonthly revenue head:\n", monthly_rev.head())

# Top products by revenue
product_rev = (
    orders.groupby(['ProductID', 'ProductName'])['LineAmount']
    .sum()
    .reset_index()
)
product_rev = product_rev.sort_values('LineAmount', ascending=False)
print("\nTop 10 products by revenue:\n", product_rev.head(10))

# Market Basket Analysis using mlxtend
try:
    from mlxtend.frequent_patterns import apriori, association_rules
except ImportError:
    raise SystemExit("Please install mlxtend: pip install mlxtend")

# Create basket (invoice-product matrix)
basket = (
    orders
    .groupby(['OrderID', 'ProductName'])['Quantity']
    .sum()
    .unstack()
    .fillna(0)
)

# Convert to 1/0
basket_binary = basket.map(lambda x: 1 if x > 0 else 0)

# Frequent itemsets
freq_items = apriori(basket_binary, min_support=0.02, use_colnames=True)
print("\nFrequent itemsets:\n", freq_items.head())

# Association rules
rules = association_rules(freq_items, metric='lift', min_threshold=1.0)
rules = rules.sort_values('lift', ascending=False)
print("\nTop 10 rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

# Save to CSV for dashboard usage
monthly_rev.to_csv('monthly_revenue.csv', index=False)
product_rev.to_csv('product_revenue.csv', index=False)
rules.to_csv('association_rules.csv', index=False)

print("\nFiles saved: monthly_revenue.csv, product_revenue.csv, association_rules.csv")