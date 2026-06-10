from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

shipments = pd.read_csv(
    BASE_DIR / "datasets" / "shipments.csv"
)

print("\n========== SHIPMENT SUMMARY ==========\n")

print(
    shipments["Shipment_Status"]
    .value_counts()
)

delayed_shipments = shipments[
    shipments["Shipment_Status"] == "Delayed"
]

print("\n========== DELAYED SHIPMENTS ==========\n")

if delayed_shipments.empty:
    print("No delayed shipments found.")

else:
    print(delayed_shipments)

delayed_shipments.to_csv(
    BASE_DIR / "datasets" / "delayed_shipments_report.csv",
    index=False
)

print("\nShipment report generated successfully.")