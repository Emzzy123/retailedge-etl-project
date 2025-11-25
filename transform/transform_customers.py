# transform/transform_customers.py
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/customers_large.csv")

def transform_customers():
    df = pd.read_csv(RAW_PATH, on_bad_lines="warn")
    df.columns = df.columns.str.strip()

    print("\n=== Transforming customers ===")
    print("Rows before cleaning:", len(df))

    df = df.dropna(subset=["customer_id", "name"])

    df["name"] = df["name"].astype(str).str.strip()
    df = df[df["name"] != ""]

    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    invalid_dates = df["signup_date"].isna().sum()
    print("Invalid or missing signup_date values:", invalid_dates)

    rows_before_dedup = len(df)
    df = df.drop_duplicates()
    print("Duplicates removed:", rows_before_dedup - len(df))

    print("Rows after cleaning:", len(df))
    print("Columns and dtypes after transform:")
    print(df.dtypes)

    return df

if __name__ == "__main__":
    transform_customers()
