CREATE TABLE transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    amount NUMERIC(12,2) NOT NULL CHECK (amount >= 0),
    transaction_hour INTEGER NOT NULL CHECK (transaction_hour BETWEEN 0 AND 23),
    account_age_days INTEGER NOT NULL CHECK (account_age_days >= 0),
    transactions_last_24h INTEGER NOT NULL CHECK (transactions_last_24h >= 0),
    international SMALLINT NOT NULL CHECK (international IN (0,1)),
    new_device SMALLINT NOT NULL CHECK (new_device IN (0,1)),
    location_mismatch SMALLINT NOT NULL CHECK (location_mismatch IN (0,1)),
    is_fraud SMALLINT NOT NULL CHECK (is_fraud IN (0,1))
);
