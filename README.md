# credit_card_fraud_detection
Hybrid Adaptive Sampling with Explainable Risk-Based Credit Card Fraud Detection (HAS-RFD)

A mini-project web application for credit card fraud detection using machine learning, hybrid sampling, risk classification and explainable fraud indicators.

Project Overview

The project described in the mini-project presentation focuses on:

Real-time fraud detection

Handling highly imbalanced transaction data

Hybrid Adaptive Sampling (clustering-based sampling + SMOTE)

Random Forest and Logistic Regression

Low / Medium / High risk classification

Explainable fraud indicators

Transaction management

Fraud alerts and notifications

The application implements these ideas as a lightweight Flask web application with SQLite.

Important: The supplied project presentation does not contain the original source code or a training dataset. Therefore, this repository uses a reproducible synthetic dataset for demonstration. Replace the synthetic training section in model.py with your real credit-card dataset before using it for research results or deployment.

Features

Register

Create a user account.

Passwords are hashed before storage.

Login

Credential verification.

Session-based access control.

Add Transaction

Amount

Date and time

Location

Location risk

Merchant risk

International transaction flag

Transaction velocity

Fraud Detection & Analysis

Hybrid sampling concept

SMOTE oversampling

Random Forest

Logistic Regression

Ensemble probability

Fraud/Genuine prediction

Risk Classification

Low

Medium

High

Explainability

Displays the transaction indicators that contributed to a high-risk assessment.

Alerts

Generates an alert when a suspicious transaction is detected.

Transaction Management

View transactions

Search/filter can be extended

Delete transactions

Logout

Clears the user session.

Technology Stack

Layer

Technology

Frontend

HTML, CSS

Backend

Python, Flask

Database

SQLite

Machine Learning

Scikit-learn

Imbalanced Learning

imbalanced-learn / SMOTE

Sampling

K-Means clustering + SMOTE

Models

Random Forest, Logistic Regression

Project Structure

HAS-RFD-Credit-Card-Fraud-Detection/
│
├── app.py
├── model.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_transaction.html
│   ├── transactions.html
│   └── analysis.html
│
└── static/
    └── style.css

Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/HAS-RFD-Credit-Card-Fraud-Detection.git
cd HAS-RFD-Credit-Card-Fraud-Detection

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

Open:

http://127.0.0.1:5000

Machine Learning Workflow

Transaction Input
       |
       v
Feature Preparation
       |
       v
Clustering-Based Adaptive Sampling
       |
       v
SMOTE Oversampling
       |
       v
+---------------------------+
| Random Forest             |
| Logistic Regression       |
+---------------------------+
       |
       v
Ensemble Fraud Probability
       |
       v
Fraud / Genuine
       |
       v
Risk Classification
Low / Medium / High
       |
       v
Explanation + Alert

Risk Classification

The demonstration model uses the averaged probability from Random Forest and Logistic Regression:

High: probability >= 0.75

Medium: probability >= 0.40 and < 0.75

Low: probability < 0.40

These thresholds can be tuned using validation data.

Dataset

No original dataset was included with the supplied project presentation, so model.py creates an imbalanced synthetic dataset using make_classification().

For a research-grade implementation, replace _build_training_data() with a real credit-card fraud dataset and perform:

Train/test split

Feature scaling

Cross-validation

Hyperparameter tuning

Precision, recall and F1 evaluation

ROC-AUC / PR-AUC

Confusion matrix

False-negative analysis

Explainability

The current demo provides human-readable risk indicators such as:

High transaction amount

Unusual transaction time

High location risk

High merchant risk

International transaction

High transaction velocity

For a more advanced implementation, SHAP or LIME can be integrated with the trained model to provide model-level feature attribution.

Security Notes

This is an academic/demo project.

Before production deployment:

Move SECRET_KEY to an environment variable.

Use HTTPS.

Add CSRF protection.

Validate and sanitize all inputs.

Add rate limiting.

Use a production database.

Secure database credentials.

Do not expose model internals or sensitive customer information.

Perform proper authentication and authorization testing.

Future Enhancements

Real credit-card fraud dataset integration

SHAP-based explainable AI dashboard

Real-time transaction streaming

Email/SMS fraud notifications

Advanced adaptive sampling

XGBoost comparison

Model performance dashboard

Confusion matrix and ROC/PR curves

Admin dashboard

Transaction search and filters

Docker deployment

Cloud deployment

References

The project presentation lists the following references:

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. — SMOTE: Synthetic Minority Over-sampling Technique, Journal of Artificial Intelligence Research, 2002.

Sahin, Y. & Duman, E. — Detecting Credit Card Fraud by Decision Trees and Support Vector Machines, 2011.

Randhawa, M., Joshi, C., & Singh, S. — Credit Card Fraud Detection Using Machine Learning and Deep Learning Techniques, IEEE Access, 2018.

Lundberg, S. & Lee, S.-I. — A Unified Approach to Interpreting Model Predictions, NeurIPS, 2017.

Chen, T. & Guestrin, C. — XGBoost: A Scalable Tree Boosting System, KDD, 2016.

Team

CB2329 — Lavanaya Shri R

CB2340 — Muthamil E

CB2347 — Rubhavashni LR

Guide: Mrs. M. Karthika, Assistant Professor, CSBS

Academic Disclaimer

This repository is intended for academic mini-project demonstration and learning purposes. It is not a financial security product and should not be used for real financial decisions without extensive validation, security testing and compliance review.
