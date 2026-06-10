from pathlib import Path
import pandas as pd

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

orders = pd.read_csv(BASE_DIR / "datasets" / "orders.csv")
inventory = pd.read_csv(BASE_DIR / "datasets" / "inventory.csv")

# Remove accidental spaces
orders["Product_ID"] = orders["Product_ID"].str.strip()
inventory["Product_ID"] = inventory["Product_ID"].str.strip()

# Calculate total quantity sold
sales_summary = (
    orders.groupby("Product_ID")["Quantity"]
    .sum()
    .reset_index()
)

print("\nSales Summary:\n")
print(sales_summary)

# Update inventory
for _, row in sales_summary.iterrows():

    product_id = row["Product_ID"]
    quantity_sold = row["Quantity"]

    current_stock = inventory.loc[
        inventory["Product_ID"] == product_id,
        "Current_Stock"
    ].iloc[0]

    new_stock = max(
        0,
        current_stock - quantity_sold
    )

    inventory.loc[
        inventory["Product_ID"] == product_id,
        "Current_Stock"
    ] = new_stock

# Add status column
inventory["Inventory_Status"] = "Healthy"

inventory.loc[
    inventory["Current_Stock"] <= 0,
    "Inventory_Status"
] = "Out of Stock"

inventory.loc[
    (inventory["Current_Stock"] > 0)
    &
    (inventory["Current_Stock"] < inventory["Reorder_Level"]),
    "Inventory_Status"
] = "Low Stock"

print("\nUpdated Inventory:\n")
print(inventory)

inventory.to_csv(
    BASE_DIR / "datasets" / "updated_inventory.csv",
    index=False
)

print("\nInventory updated successfully.")