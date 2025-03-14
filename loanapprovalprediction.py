# -*- coding: utf-8 -*-
"""LoanApprovalPrediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yVcKpsnUE3uHZMk1MQzOSdYmK2WvqRDt
"""

from google.colab import drive
drive.mount('/content/gdrive')

import os
os.environ["KAGGLE_CONFIG_DIR"] = '/content/gdrive/MyDrive/Kaggle/LoanApproval'

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv(r'/content/gdrive/MyDrive/Kaggle/LoanApproval/LoanPrediction.csv')
pd.set_option('display.max_colwidth', None)
df.head(10)

# Define columns to encode
columns_to_encode = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical columns
for col in columns_to_encode:
    df[col] = label_encoder.fit_transform(df[col].astype(str))

# Display the encoded dataframe
df.head()

df.isnull().sum()

# Drop the "Loan_ID" column
df.drop(columns=['Loan_ID'], inplace=True)

# Replace missing values with mean
df.fillna(df.mean(), inplace=True)

# Display the dataframe with imputed missing values
print(df)

df.head(100)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Display correlation matrix
print(correlation_matrix)

# Visualize correlation matrix using a heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

from sklearn.model_selection import train_test_split

# Assuming your data is stored in a DataFrame called 'df'

# Separate features (X) and target variable (y)
X = df.drop(columns=['Loan_Status'])  # Features
y = df['Loan_Status']  # Target variable

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now you have X_train (features for training), X_test (features for testing),
# y_train (target variable for training), and y_test (target variable for testing)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import numpy as np

# Define a dictionary to store models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC(probability=True),  # Setting probability=True for SVM
    "Neural Network": MLPClassifier()
}

# Iterate over each model
for name, model in models.items():
    print("Model:", name)
    # Train the model
    model.fit(X_train, y_train)

    # Predict on train and test set
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Compute performance metrics
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    train_precision = precision_score(y_train, y_train_pred)
    test_precision = precision_score(y_test, y_test_pred)

    train_recall = recall_score(y_train, y_train_pred)
    test_recall = recall_score(y_test, y_test_pred)

    train_f1 = f1_score(y_train, y_train_pred)
    test_f1 = f1_score(y_test, y_test_pred)

    # AUC score can only be computed for binary classification tasks
    if len(np.unique(y_train)) == 2 and len(np.unique(y_test)) == 2:
        train_auc = roc_auc_score(y_train, model.predict_proba(X_train)[:, 1])
        test_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    else:
        train_auc = np.nan
        test_auc = np.nan

    # Print results
    print("Train Metrics:")
    print("Accuracy:", train_accuracy)
    print("Precision:", train_precision)
    print("Recall:", train_recall)
    print("F1-score:", train_f1)
    print("AUC:", train_auc)
    print("\nTest Metrics:")
    print("Accuracy:", test_accuracy)
    print("Precision:", test_precision)
    print("Recall:", test_recall)
    print("F1-score:", test_f1)
    print("AUC:", test_auc)
    print("\n---------------------------\n")

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB

# Initialize classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting Machines": GradientBoostingClassifier(),
    "Support Vector Machines": SVC(probability=True),  # Enable probability estimation for SVM
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Artificial Neural Network": MLPClassifier(),
    "LightGBM": LGBMClassifier(),
    "XGBoost": XGBClassifier(),
    "Naive Bayes": GaussianNB()
}

# Evaluation metrics
metrics = ["Precision", "Recall", "F1", "Accuracy", "AUC"]

# Train and evaluate models
for name, classifier in classifiers.items():
    print(f"Training and evaluating {name}...")
    classifier.fit(X_train, y_train)

    # Predictions
    y_train_pred = classifier.predict(X_train)
    y_test_pred = classifier.predict(X_test)

    # Use decision_function for SVM
    if name == "Support Vector Machines":
        train_probs = classifier.decision_function(X_train)
        test_probs = classifier.decision_function(X_test)
    else:
        train_probs = classifier.predict_proba(X_train)[:, 1]
        test_probs = classifier.predict_proba(X_test)[:, 1]

    # Calculate evaluation metrics
    train_metrics = [
        precision_score(y_train, y_train_pred),
        recall_score(y_train, y_train_pred),
        f1_score(y_train, y_train_pred),
        accuracy_score(y_train, y_train_pred),
        roc_auc_score(y_train, train_probs)
    ]
    test_metrics = [
        precision_score(y_test, y_test_pred),
        recall_score(y_test, y_test_pred),
        f1_score(y_test, y_test_pred),
        accuracy_score(y_test, y_test_pred),
        roc_auc_score(y_test, test_probs)
    ]

    # Print results
    print("\tTrain Metrics:")
    for metric_name, metric_value in zip(metrics, train_metrics):
        print(f"\t\t{metric_name}: {metric_value:.4f}")

    print("\tTest Metrics:")
    for metric_name, metric_value in zip(metrics, test_metrics):
        print(f"\t\t{metric_name}: {metric_value:.4f}")
    print("\n")