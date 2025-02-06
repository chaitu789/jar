import pandas as pd

# Load datasets
list_of_orders = pd.read_csv(r"C:\Users\HP\Downloads\List_of_Orders_55FFC79CF8.csv")
order_details = pd.read_csv(r"C:\Users\HP\Downloads\Order_Details_19795F61CF.csv")

# Merge datasets on 'Order ID'
merged_df = pd.merge(list_of_orders, order_details, on="Order ID")

category_sales = merged_df.groupby("Category").agg(
    Total_Sales=("Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Order_Count=("Order ID", "count")
).reset_index()

# Calculate additional metrics
category_sales["Avg_Profit_Per_Order"] = category_sales["Total_Profit"] / category_sales["Order_Count"]
category_sales["Profit_Margin"] = (category_sales["Total_Profit"] / category_sales["Total_Sales"]) * 100

# Identify top and underperforming categories
top_category = category_sales.loc[category_sales["Profit_Margin"].idxmax()]
underperforming_category = category_sales.loc[category_sales["Profit_Margin"].idxmin()]

# Display results
print(category_sales)
print("\nTop Performing Category:\n", top_category)
print("\nUnderperforming Category:\n", underperforming_category)

# Analysis of performance differences
if top_category["Profit_Margin"] > 20:
    print(f"\n{top_category['Category']} performs well due to high profit margins. Possible reasons:")
    print("- High demand and premium pricing")
    print("- Low cost of goods sold (COGS)")
    print("- Efficient supply chain and low operational costs")

if underperforming_category["Profit_Margin"] < 10:
    print(f"\n{underperforming_category['Category']} is underperforming due to low margins. Possible reasons:")
    print("- High competition leading to price reductions")
    print("- High COGS or operational costs")
    print("- Low demand or high return rates")