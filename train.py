from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_auc_score, precision_score, recall_score, f1_score)

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "transactions.csv"
MODEL_DIR = BASE / "models"
REPORT_DIR = BASE / "reports"
FEATURES = [
    "amount", "transaction_hour", "account_age_days",
    "transactions_last_24h", "international", "new_device", "location_mismatch"
]

def main():
    df = pd.read_csv(DATA)
    X, y = df[FEATURES], df["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=42
        ))
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    metrics = {
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1": f1_score(y_test, predictions, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probabilities),
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
        "classification_report": classification_report(
            y_test, predictions, zero_division=0, output_dict=True
        )
    }
    MODEL_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "fraud_detection_model.joblib")
    (REPORT_DIR / "evaluation.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print("Evaluation on held-out synthetic test set:")
    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix (rows=actual, columns=predicted):")
    print(confusion_matrix(y_test, predictions))
    print(f"ROC-AUC: {metrics['roc_auc']:.3f}")
    print("Saved model to models/fraud_detection_model.joblib")

if __name__ == "__main__":
    main()
