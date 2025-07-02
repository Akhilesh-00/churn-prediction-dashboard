import pandas as pd
import joblib

# Load files
model = joblib.load("churn_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Load dataset
df_full = pd.read_csv("Telco-Customer-Churn.csv")
df_full['Churn'] = df_full['Churn'].map({'Yes': 1, 'No': 0})

# Preprocess (One-Hot Encoding)
df_model_input = pd.get_dummies(df_full)
df_model_input = df_model_input.reindex(columns=feature_names, fill_value=0)

# Predict
df_full['Churn_Prob'] = model.predict_proba(df_model_input)[:, 1]
df_full['Churn_Prediction'] = model.predict(df_model_input)

# Save to CSV
df_full.to_csv("churn_predictions.csv", index=False)
print("✅ churn_predictions.csv saved successfully!")
