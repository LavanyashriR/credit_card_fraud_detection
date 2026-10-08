

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# ---------------------------------------------------
# 1. Create Sample Transaction Dataset
# ---------------------------------------------------

np.random.seed(42)

# Features:
# amount, transaction_hour, location_risk,
# merchant_risk, international, transaction_velocity

X = np.random.rand(1000, 6)

# Convert some features into useful ranges
X[:, 0] = X[:, 0] * 5000       # Transaction amount
X[:, 1] = X[:, 1] * 24         # Hour
X[:, 2] = X[:, 2]              # Location risk
X[:, 3] = X[:, 3]              # Merchant risk
X[:, 4] = (X[:, 4] > 0.8)      # International
X[:, 5] = X[:, 5] * 10         # Transaction velocity

# Create imbalanced target
y = np.zeros(1000, dtype=int)

# Sample fraud transactions
fraud_indices = np.random.choice(1000, 50, replace=False)
y[fraud_indices] = 1

print("Original Dataset")
print("Genuine transactions:", sum(y == 0))
print("Fraud transactions:", sum(y == 1))


# ---------------------------------------------------
# 2. Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------------------
# 3. Handle Imbalanced Data using SMOTE
# ---------------------------------------------------

smote = SMOTE(random_state=42)

X_train_balanced, y_train_balanced = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter SMOTE")
print("Genuine:", sum(y_train_balanced == 0))
print("Fraud:", sum(y_train_balanced == 1))


# ---------------------------------------------------
# 4. Random Forest Model
# ---------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest.fit(
    X_train_balanced,
    y_train_balanced
)

rf_prediction = random_forest.predict(X_test)


# ---------------------------------------------------
# 5. Logistic Regression Model
# ---------------------------------------------------

logistic_model = LogisticRegression(
    max_iter=1000
)

logistic_model.fit(
    X_train_balanced,
    y_train_balanced
)

lr_prediction = logistic_model.predict(X_test)


# ---------------------------------------------------
# 6. Model Evaluation
# ---------------------------------------------------

print("\nRandom Forest Accuracy:")
print(accuracy_score(y_test, rf_prediction))

print("\nRandom Forest Report:")
print(classification_report(y_test, rf_prediction))

print("\nLogistic Regression Accuracy:")
print(accuracy_score(y_test, lr_prediction))


# ---------------------------------------------------
# 7. Fraud Detection Function
# ---------------------------------------------------

def detect_fraud(amount, hour, location_risk,
                 merchant_risk, international, velocity):

    transaction = np.array([[
        amount,
        hour,
        location_risk,
        merchant_risk,
        international,
        velocity
    ]])

    # Get fraud probabilities
    rf_probability = random_forest.predict_proba(transaction)[0][1]
    lr_probability = logistic_model.predict_proba(transaction)[0][1]

    # Average the two model predictions
    fraud_probability = (
        rf_probability + lr_probability
    ) / 2

    # Fraud / Genuine
    if fraud_probability >= 0.5:
        result = "FRAUD"
    else:
        result = "GENUINE"

    # Risk classification
    if fraud_probability >= 0.75:
        risk = "HIGH"
    elif fraud_probability >= 0.40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # Simple explanation
    reasons = []

    if amount > 3000:
        reasons.append("High transaction amount")

    if hour < 6 or hour > 22:
        reasons.append("Unusual transaction time")

    if location_risk > 0.7:
        reasons.append("High location risk")

    if merchant_risk > 0.7:
        reasons.append("High merchant risk")

    if international == 1:
        reasons.append("International transaction")

    if velocity > 7:
        reasons.append("High transaction velocity")

    if not reasons:
        reasons.append("No major risk indicators")

    return result, risk, fraud_probability, reasons


# ---------------------------------------------------
# 8. Test a New Transaction
# ---------------------------------------------------

print("\n--------------------------------")
print("NEW TRANSACTION")
print("--------------------------------")

amount = 4500
hour = 2
location_risk = 0.85
merchant_risk = 0.75
international = 1
velocity = 8

result, risk, probability, reasons = detect_fraud(
    amount,
    hour,
    location_risk,
    merchant_risk,
    international,
    velocity
)

print("Transaction Amount : ₹", amount)
print("Transaction Hour   :", hour)
print("Result             :", result)
print("Risk Level         :", risk)
print("Fraud Probability  :", round(probability * 100, 2), "%")

print("\nExplanation:")
for reason in reasons:
    print("-", reason)
