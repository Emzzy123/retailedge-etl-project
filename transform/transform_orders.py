# transform/transform_orders.py
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/orders_large.csv")

def transform_orders():
    df = pd.read_csv(RAW_PATH, on_bad_lines="warn")
    df.columns = df.columns.str.strip()

    print("\n=== Transforming orders ===")
    print("Rows before cleaning:", len(df))

    df = df.dropna(subset=["order_id", "customer_id"])

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    invalid_dates = df["order_date"].isna().sum()
    print("Invalid order_date values (will be dropped):", invalid_dates)
    df = df.dropna(subset=["order_date"])

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    invalid_amounts = df["amount"].isna().sum()
    print("Missing or invalid amount values:", invalid_amounts)

    df["product_category"] = (
        df["product_category"]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Rows after cleaning:", len(df))
    print("Columns and dtypes after transform:")
    print(df.dtypes)

    return df

if __name__ == "__main__":
    transform_orders()
