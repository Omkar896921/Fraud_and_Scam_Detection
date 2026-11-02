# Classification metrics guide

- **Confusion matrix**: counts true negatives, false positives, false negatives and true positives.
- **Precision**: among transactions flagged as fraud, the share that are fraud.
- **Recall**: among actual fraud cases, the share caught by the model.
- **F1-score**: harmonic mean of precision and recall.
- **ROC-AUC**: ranking ability across thresholds; interpret alongside precision-recall metrics when the positive class is rare.

## Key trade-off
- False positive: legitimate transaction flagged for review.
- False negative: fraudulent transaction missed.

Do not use accuracy alone for an imbalanced dataset. The best threshold depends on review capacity, customer impact and fraud losses.
