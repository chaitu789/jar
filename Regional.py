import pandas as pd

# Load datasets
orders_df = pd.read_csv(r"C:\Users\HP\Downloads\List_of_Orders_55FFC79CF8.csv")
order_details_df = pd.read_csv(r"C:\Users\HP\Downloads\Order_Details_19795F61CF.csv")

# -------------------------------
# Step 2: Identify Top 5 States by Order Count (from List_of_Orders)
# -------------------------------
state_order_counts = orders_df.groupby("State")["Order ID"].count().reset_index(name='Order_Count')
top5_states = state_order_counts.sort_values("Order_Count", ascending=False).head(5)

print("Top 5 States by Order Count:")
print(top5_states)

# -------------------------------
# Step 3: Merge Datasets on 'Order ID'
# -------------------------------
merged_df = pd.merge(orders_df, order_details_df, on="Order ID")

# -------------------------------
# Step 4: For Top 5 States, Calculate Total Sales and Average Profit
# -------------------------------
# Filter merged data for the top 5 states
top5_states_data = merged_df[merged_df["State"].isin(top5_states["State"])]

state_metrics_top5 = top5_states_data.groupby("State").agg(
    Total_Sales=("Amount", "sum"),
    Average_Profit=("Profit", "mean"),
    Order_Count=("Order ID", "nunique")
).reset_index()

print("\nMetrics for Top 5 States (Total Sales, Average Profit, Order Count):")
print(state_metrics_top5)

# -------------------------------
# Step 5: Highlight Regional Disparities in Sales/Profitability
# -------------------------------
# Calculate overall state-level metrics for all states
state_metrics = merged_df.groupby("State").agg(
    Total_Sales=("Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Order_Count=("Order ID", "nunique")
).reset_index()
state_metrics["Profit_Margin"] = (state_metrics["Total_Profit"] / state_metrics["Total_Sales"]) * 100

print("\nOverall State-Level Metrics (Sorted by Profit Margin):")
print(state_metrics.sort_values("Profit_Margin"))

# Identify states with low profit margins (e.g., below 10%)
priority_states = state_metrics[state_metrics["Profit_Margin"] < 10].sort_values("Profit_Margin")
if not priority_states.empty:
    print("\nPriority States for Improvement (Profit Margin < 10%):")
    print(priority_states)
else:
    print("\nNo states found with Profit Margin below the 10% threshold.")

# Additionally, calculate city-level metrics for further granularity
city_metrics = merged_df.groupby("City").agg(
    Total_Sales=("Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Order_Count=("Order ID", "nunique")
).reset_index()
city_metrics["Profit_Margin"] = (city_metrics["Total_Profit"] / city_metrics["Total_Sales"]) * 100

print("\nCity-Level Metrics (Sorted by Profit Margin - Bottom 10 Cities):")
print(city_metrics.sort_values("Profit_Margin").head(10))

# -------------------------------
# Step 6: Suggest Regions/Cities for Improvement
# -------------------------------
print("\nSuggestions for Improvement:")
print("- Regions (states or cities) with low profit margins (for example, below 10%) may be facing challenges such as:")
print("  • High operational costs")
print("  • Intense competition or pricing pressures")
print("  • Inefficient supply chain or cost structure")
print("- It is recommended to conduct a deeper analysis in these areas to determine the root causes.")
print("- Based on the above metrics, focus improvement efforts (like cost optimization, targeted marketing, or renegotiation of supplier contracts) on the identified priority states and cities.")