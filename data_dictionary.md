# Data dictionary

All data is synthetic and generated for learning. It contains no real banking information.

| Field | Meaning |
|---|---|
| transaction_id | Synthetic transaction key |
| amount | Sample transaction amount (illustrative units) |
| transaction_hour | Hour of day, 0–23 |
| account_age_days | Account age in days |
| transactions_last_24h | Count of recent transactions |
| international | 1 if international flag is on |
| new_device | 1 if new-device flag is on |
| location_mismatch | 1 if location mismatch flag is on |
| is_fraud | Target: 1 synthetic fraud, 0 normal |

The generated patterns are simplistic and do not represent real fraud behaviour.
