# Fraud & Scam Detection

An end-to-end binary classification project that flags potentially fraudulent transactions.

## Dataset and safety
`data/transactions.csv` is fully synthetic demonstration data. It contains no real customer, bank or transaction records. This project is for education only and is **not** a production fraud-control system.

## Features
- Transaction amount
- Transaction hour
- Account age in days
- Transaction count in last 24 hours
- International transaction flag
- New device flag
- Location mismatch flag

Target: `is_fraud` (1 = synthetic fraud example, 0 = normal example).

## Setup (Python 3.10+)
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```bash
python src/validate_data.py
python src/train.py
streamlit run src/app.py
```

## What is implemented
- Stratified train/test split to preserve rare-class proportion.
- StandardScaler + LogisticRegression in a Pipeline.
- `class_weight='balanced'` to give the minority class more influence.
- Confusion matrix, precision, recall, F1 and ROC-AUC.
- Saved model and evaluation report.

## Important interpretation
Fraud detection is imbalanced: accuracy alone can be misleading. Review precision (how many flagged transactions are actually fraud), recall (how many fraud cases are caught), and the operational cost of false positives/false negatives. Threshold tuning and temporal validation are important before any real deployment.
