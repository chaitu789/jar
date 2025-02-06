import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\Sales_target_DD2E9B96A0.csv")

# Convert 'Month of Order Date' to datetime format
df['Month of Order Date'] = pd.to_datetime(df['Month of Order Date'], format="%b-%y")
df = df.sort_values(by='Month of Order Date').reset_index(drop=True)
print("\nData with Converted Dates:")
print(df)

# Step 3: Calculate Month-over-Month percentage change
df['Percentage Change'] = df['Target'].pct_change() * 100
print("\nData with Percentage Change:")
print(df)

# Step 4: Analyze trends to identify significant fluctuations
# (Adjust the threshold based on what is considered significant for your analysis)
threshold = 1  # Example threshold for significant change
significant_changes = df[df['Percentage Change'].abs() > threshold]
print("\nSignificant Fluctuations (Threshold > 1%):")
print(significant_changes)
# Proceed with analysis
print(df.head())  # Check if dates are correctly formatted