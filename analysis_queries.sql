-- Class distribution and fraud prevalence
SELECT is_fraud, COUNT(*) AS transaction_count,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM transactions
GROUP BY is_fraud;

-- Average amount by target class
SELECT is_fraud, ROUND(AVG(amount), 2) AS average_amount
FROM transactions
GROUP BY is_fraud;

-- Fraud examples by transaction hour
SELECT transaction_hour, COUNT(*) AS flagged_examples
FROM transactions
WHERE is_fraud = 1
GROUP BY transaction_hour
ORDER BY transaction_hour;
