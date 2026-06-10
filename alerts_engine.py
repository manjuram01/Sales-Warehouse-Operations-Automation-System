from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

inventory = pd.read_csv(
    BASE_DIR / "datasets" / "updated_inventory.csv"
)

# Low stock products
low_stock = inventory[
    (inventory["Current_Stock"] > 0) &
    (inventory["Current_Stock"] < inventory["Reorder_Level"])
]

# Out of stock products
out_of_stock = inventory[
    inventory["Current_Stock"] <= 0
]

print("\n========== LOW STOCK ==========\n")

if low_stock.empty:
    print("No low stock products")

else:
    print(
        low_stock[
            [
                "Product_Name",
                "Current_Stock",
                "Reorder_Level"
            ]
        ]
    )

print("\n========== OUT OF STOCK ==========\n")

if out_of_stock.empty:
    print("No stockout products")

else:
    print(
        out_of_stock[
            [
                "Product_Name",
                "Current_Stock",
                "Reorder_Level"
            ]
        ]
    )

# Save reports
low_stock.to_csv(
    BASE_DIR / "datasets" / "low_stock_alerts.csv",
    index=False
)

out_of_stock.to_csv(
    BASE_DIR / "datasets" / "out_of_stock_alerts.csv",
    index=False
)

print("\nAlert reports created successfully.")