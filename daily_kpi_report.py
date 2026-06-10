from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

# Load datasets
orders = pd.read_csv(
    BASE_DIR / "datasets" / "orders.csv"
)

products = pd.read_csv(
    BASE_DIR / "datasets" / "products.csv"
)

customers = pd.read_csv(
    BASE_DIR / "datasets" / "customers.csv"
)

# Merge orders + products
sales = pd.merge(
    orders,
    products,
    on="Product_ID"
)

# Revenue calculation
sales["Revenue"] = (
    sales["Quantity"]
    * sales["Unit_Price"]
)

# KPI 1
total_orders = sales["Order_ID"].nunique()

# KPI 2
total_units_sold = sales["Quantity"].sum()

# KPI 3
total_revenue = sales["Revenue"].sum()

# KPI 4
top_product = (
    sales.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# KPI 5
top_product_units = (
    sales.groupby("Product_Name")["Quantity"]
    .sum()
    .max()
)

# Merge customer info
customer_sales = pd.merge(
    orders,
    customers,
    on="Customer_ID"
)

top_customer = (
    customer_sales["Customer_Name"]
    .value_counts()
    .index[0]
)

top_city = (
    customer_sales["City"]
    .value_counts()
    .index[0]
)

print("\n========== EXECUTIVE KPI REPORT ==========\n")

print(f"Total Orders       : {total_orders}")
print(f"Total Units Sold   : {total_units_sold}")
print(f"Total Revenue      : ₹{total_revenue:,.0f}")
print(f"Top Product        : {top_product}")
print(f"Units Sold         : {top_product_units}")
print(f"Top Customer       : {top_customer}")
print(f"Top City           : {top_city}")

# Save report
kpi_df = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Units Sold",
        "Total Revenue",
        "Top Product",
        "Top Customer",
        "Top City"
    ],
    "Value": [
        total_orders,
        total_units_sold,
        total_revenue,
        top_product,
        top_customer,
        top_city
    ]
})

kpi_df.to_csv(
    BASE_DIR / "datasets" / "executive_kpi_report.csv",
    index=False
)

print("\nExecutive KPI report generated.")