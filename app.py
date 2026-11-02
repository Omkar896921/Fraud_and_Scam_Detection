from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE / "models" / "fraud_detection_model.joblib"
st.set_page_config(page_title="Fraud Detection Demo", layout="centered")
st.title("Fraud & Scam Detection")
st.caption("Educational demonstration using synthetic data only.")

if not MODEL_PATH.exists():
    st.error("Trained model not found. Run: python src/train.py")
    st.stop()

model = joblib.load(MODEL_PATH)
with st.form("transaction_form"):
    amount = st.number_input("Transaction amount", min_value=0.0, value=250.0, step=50.0)
    hour = st.slider("Transaction hour", 0, 23, 14)
    age = st.number_input("Account age (days)", min_value=1, value=365)
    count = st.number_input("Transactions in last 24 hours", min_value=0, value=3)
    international = st.selectbox("International transaction?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    new_device = st.selectbox("New device?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    mismatch = st.selectbox("Location mismatch?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    submitted = st.form_submit_button("Assess transaction")

if submitted:
    sample = pd.DataFrame([{
        "amount": amount, "transaction_hour": hour, "account_age_days": age,
        "transactions_last_24h": count, "international": international,
        "new_device": new_device, "location_mismatch": mismatch
    }])
    probability = float(model.predict_proba(sample)[0, 1])
    st.metric("Model-estimated fraud probability", f"{probability:.1%}")
    if probability >= 0.5:
        st.warning("Model flags this sample transaction for review.")
    else:
        st.success("Model does not flag this sample transaction at the current threshold.")
    st.info("This is not a bank decision or a real fraud assessment. Never use this demo to approve, reject or block real transactions.")
