# extract/extract_returns.py
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/returns_large.csv")
REQUIRED_COLUMNS = ["order_id", "return_date", "return_reason"]

def extract_returns():
    if not RAW_PATH.exists():
        print(f"ERROR: File not found at {RAW_PATH}")
        return None

    df = pd.read_csv(RAW_PATH, on_bad_lines="warn")
    df.columns = df.columns.str.strip()


    print("\n=== Returns: basic info ===")
    print(f"File path: {RAW_PATH}")
    print(f"Number of rows loaded: {df.shape[0]}")
    print(f"Columns found: {list(df.columns)}")

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        print(f"WARNING: Missing required columns: {missing_cols}")
    else:
        print("All required columns are present.")

    print("\nDetected data types:")
    print(df.dtypes)

    return df

if __name__ == "__main__":
    extract_returns()
