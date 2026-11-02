from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "transactions.csv"
REQUIRED = {
    "transaction_id", "amount", "transaction_hour", "account_age_days",
    "transactions_last_24h", "international", "new_device",
    "location_mismatch", "is_fraud"
}

def main():
    df = pd.read_csv(DATA)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if df[list(REQUIRED)].isna().any().any():
        raise ValueError("Missing values found.")
    if not set(df["is_fraud"].unique()).issubset({0, 1}):
        raise ValueError("Target must contain only 0 and 1.")
    if not df["transaction_hour"].between(0, 23).all():
        raise ValueError("transaction_hour must be between 0 and 23.")
    print(f"VALID: {len(df)} rows | fraud examples: {int(df.is_fraud.sum())} "
          f"({df.is_fraud.mean():.2%})")

if __name__ == "__main__":
    main()
