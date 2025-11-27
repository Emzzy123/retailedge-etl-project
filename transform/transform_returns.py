import pandas as pd
from pathlib import Path

RETURNS_PATH = Path("data/raw/returns_large.csv")
ORDERS_PATH = Path("data/raw/orders_large.csv")

def transform_returns():
    returns_df = pd.read_csv(RETURNS_PATH, on_bad_lines="warn")
    orders_df = pd.read_csv(ORDERS_PATH, on_bad_lines="warn")

    returns_df.columns = returns_df.columns.str.strip()
    orders_df.columns = orders_df.columns.str.strip()

    print("\n=== Transforming returns ===")
    print("Rows before cleaning:", len(returns_df))

    valid_order_ids = set(orders_df["order_id"].dropna().unique())
    before_filter = len(returns_df)
    returns_df = returns_df[returns_df["order_id"].isin(valid_order_ids)]
    removed = before_filter - len(returns_df)
    print("Rows removed with order_id not found in orders:", removed)

    returns_df["return_date"] = pd.to_datetime(returns_df["return_date"], errors="coerce")
    invalid_dates = returns_df["return_date"].isna().sum()
    print("Invalid or missing return_date values:", invalid_dates)

    print("Rows after cleaning:", len(returns_df))
    print("Columns and dtypes after transform:")
    print(returns_df.dtypes)

    return returns_df

if _name_ == "_main_":
    transform_returns()