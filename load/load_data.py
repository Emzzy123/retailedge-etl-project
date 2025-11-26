import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))


# load/load_data.py
import pandas as pd
from pathlib import Path

from transform.transform_customers import transform_customers
from transform.transform_orders import transform_orders
from transform.transform_returns import transform_returns

DATA_RAW = Path("data/raw")
DATA_PROCESSED = Path("data/processed")


def load_dataset(name: str, raw_filename: str, transform_fn, output_filename: str):
    raw_path = DATA_RAW / raw_filename
    processed_path = DATA_PROCESSED / output_filename

    raw_df = pd.read_csv(raw_path, on_bad_lines="warn")
    raw_df.columns = raw_df.columns.str.strip()
    rows_in = len(raw_df)
    nulls_before = raw_df.isna().sum().sum()

    cleaned_df = transform_fn()
    rows_out = len(cleaned_df)
    nulls_after = cleaned_df.isna().sum().sum()

    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(processed_path, index=False)

    print(f"\n=== {name} LOAD SUMMARY ===")
    print(f"Input rows: {rows_in}")
    print(f"Output rows: {rows_out}")
    print(f"Rows removed (nulls/invalid): {rows_in - rows_out}")
    print(f"Nulls before: {nulls_before}")
    print(f"Nulls after: {nulls_after}")
    print(f"File saved to: {processed_path}")


def run_load_pipeline():
    load_dataset(
        name="Customers",
        raw_filename="customers_large.csv",
        transform_fn=transform_customers,
        output_filename="cleaned_customers.csv",
    )

    load_dataset(
        name="Orders",
        raw_filename="orders_large.csv",
        transform_fn=transform_orders,
        output_filename="cleaned_orders.csv",
    )

    load_dataset(
        name="Returns",
        raw_filename="returns_large.csv",
        transform_fn=transform_returns,
        output_filename="cleaned_returns.csv",
    )


if __name__ == "__main__":
    run_load_pipeline()
