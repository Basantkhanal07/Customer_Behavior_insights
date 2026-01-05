import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- Load trained model ---
MODEL_PATH = "models/churn_model.pkl"
pipe = joblib.load(MODEL_PATH)

# --- Streamlit UI ---
st.set_page_config(page_title="Customer Churn Predictor")
st.title("📊 Customer Churn Prediction")

# Input fields
age = st.number_input("Age", 18, 100, 30)
income = st.number_input("Annual Income", 10000, 200000, 50000)
spending = st.slider("Spending Score", 1, 100, 50)
gender = st.selectbox("Gender", ["Male", "Female"])
history = st.selectbox("Purchase History", ["Low", "Medium", "High"])

# Predict button
if st.button("Predict Churn"):
    # Prepare input as DataFrame
    input_df = pd.DataFrame([{
        "age": age,
        "annual_income": income,
        "spending_score": spending,
        "gender": gender,
        "purchase_history": history
    }])

    # Predict
    prob = pipe.predict_proba(input_df)[0][1]
    pred = int(prob >= 0.5)

    # Display result
    if pred == 1:
        st.error(f"⚠ Customer likely to churn (Risk: {prob:.2%})")
    else:
        st.success(f"✅ Customer likely to stay (Confidence: {1-prob:.2%})")
