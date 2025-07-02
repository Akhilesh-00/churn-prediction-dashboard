# 📉 Telco Customer Churn Prediction Dashboard

A complete data science project to predict customer churn using a machine learning model trained in Google Colab, with results visualized in an interactive Power BI dashboard.

---

## 🚀 Project Overview

This project identifies customers likely to churn from a telecom service using historical customer data. A machine learning model is trained to predict churn probabilities, and the output is used to build a professional, user-friendly Power BI dashboard for visual analysis and stakeholder decision-making.

---

## 🛠️ Tools & Technologies

- **Python (Colab)**: Model training and predictions using scikit-learn
- **Pandas & NumPy**: Data cleaning and preprocessing
- **Plotly**: Exploratory data visualization
- **Joblib**: Saving and loading trained models
- **Power BI**: Visual storytelling and dashboard design

---

## 📁 Project Structure

| File / Folder              | Description |
|---------------------------|-------------|
| `Churn_Predictions.ipynb` | Main Google Colab notebook (training + prediction) |
| `Telco-Customer-Churn.csv`| Dataset used for training and inference |
| `churn_model.pkl`         | Saved trained model |
| `feature_names.pkl`       | Feature list used in the model |
| `churn_predictions.csv`   | Output with churn predictions and probabilities |
| `ChurnDashboard.pbix`     | Final Power BI dashboard file |
| `README.md`               | Project overview and instructions |

---

## 🧠 Model Logic

- Trained using a classification algorithm (e.g., Random Forest / XGBoost)
- Input features were preprocessed and one-hot encoded
- Predictions included:
  - `Churn_Prediction` (0 = Stay, 1 = Churn)
  - `Churn_Prob` (probability of churn)

---

## 📊 Power BI Dashboard Features

- **Churn Distribution**: Breakdown of churned vs. non-churned customers  
- **Customer Segmentation**: Tenure, contract type, monthly charges vs. churn  
- **Predictive Scatter**: Visualizes churn probability by customer metrics  
- **Slicers**: Interactive filters (e.g., contract, internet service, etc.)  
- **KPIs**: High-level indicators on churn rate, monthly charges, etc.



---

## 📌 How to Use

1. Open the `Churn_Predictions.ipynb` notebook in Google Colab
2. Run the pipeline to generate `churn_predictions.csv`
3. Load the `csv` into Power BI to build the visuals
4. Use slicers and visuals to explore trends and churn risk

---

## 👤 Author

**Akhilesh Ramkumar**  
_Data Analyst | ML Enthusiast | Dashboard Developer_

---

## 🌐 Connect

- [LinkedIn](https://www.linkedin.com/in/akhilesh-ramkumar/)
- [GitHub](https://github.com/Akhilesh-00)

---

