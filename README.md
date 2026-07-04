# Diabetes Prediction using Logistic Regression

## Project Overview

This project implements a **Logistic Regression** model to predict whether a patient is likely to have diabetes using the **Pima Indians Diabetes Dataset**.

The project includes:
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Logistic Regression Model
- Model Evaluation
- Feature Interpretation
- Model Deployment using Streamlit

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Dataset

The project uses the **Pima Indians Diabetes Dataset**, which contains medical information such as:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

The target variable is **Outcome**, where:
- **0** = No Diabetes
- **1** = Diabetes

---

## Project Workflow

1. Load the dataset
2. Perform Exploratory Data Analysis (EDA)
3. Handle missing values
4. Split the dataset into training and testing sets
5. Scale the features using StandardScaler
6. Train the Logistic Regression model
7. Evaluate the model using classification metrics
8. Interpret feature importance
9. Save the trained model using Joblib
10. Deploy the model with a Streamlit web application

---

## Evaluation Metrics

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

---

## Project Files

- **LogisticRegression.ipynb** – Complete machine learning workflow
- **app.py** – Streamlit web application
- **model.pkl** – Trained Logistic Regression model
- **scaler.pkl** – Saved StandardScaler

---

## How to Run

1. Install the required libraries

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn joblib
```

2. Run the Streamlit application

```bash
streamlit run app.py
```

---

## Application Features

- User-friendly interface
- Patient data input
- Diabetes prediction
- Prediction probability
- Real-time results

---

## Conclusion

A Logistic Regression model was successfully developed to predict diabetes using the Pima Indians Diabetes Dataset. After preprocessing and feature scaling, the model achieved good classification performance. Glucose, BMI, and Age were identified as the most influential features. The trained model was deployed as an interactive Streamlit web application for real-time predictions.

