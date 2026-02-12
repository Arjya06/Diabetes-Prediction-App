import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime
from sklearn.preprocessing import StandardScaler

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="AI Diabetes Risk Dashboard",
    page_icon="🧬",
    layout="wide"
)

# =====================
# LOAD MODEL
# =====================
import joblib
model = joblib.load("diabetes_model.pkl")



# =====================
# CUSTOM CSS (GLASS UI)
# =====================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.glass {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.metric-box {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.big-font {
    font-size: 30px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================
st.markdown("<h1 style='text-align:center;'>🧬 AI Diabetes Risk Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict Diabetes Using Machine Learning</p>", unsafe_allow_html=True)

# =====================
# INPUT SECTION
# =====================
st.markdown("### 🧾 Patient Details")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("🤰 Pregnancies", 0, 20, 1)
    glucose = st.number_input("🍬 Glucose Level", 0, 200, 120)
    blood_pressure = st.number_input("🩸 Blood Pressure", 0, 150, 70)
    skin_thickness = st.number_input("📏 Skin Thickness", 0, 100, 20)

with col2:
    insulin = st.number_input("💉 Insulin", 0, 900, 80)
    bmi = st.number_input("⚖ BMI", 0.0, 70.0, 30.0)
    dpf = st.number_input("🧬 Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.number_input("🎂 Age", 1, 120, 35)

# =====================
# PREDICT BUTTON
# =====================
if st.button("🚀 Predict Risk"):

    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # =====================
    # RESULT DISPLAY
    # =====================
    st.markdown("## 🧾 Prediction Result")

    if prediction == 1:
        st.error(f"⚠ High Diabetes Risk ({probability*100:.2f}%)")
        risk_text = "High Risk"
    else:
        st.success(f"✅ Low Diabetes Risk ({(1-probability)*100:.2f}%)")
        risk_text = "Low Risk"

    # =====================
    # PROGRESS BAR
    # =====================
    st.markdown("### 📊 Risk Probability")
    st.progress(float(probability))

    # =====================
    # RISK EXPLANATION
    # =====================
    st.markdown("### 🧠 AI Explanation")

    if probability > 0.7:
        st.warning("Very high probability. Immediate medical consultation recommended.")
    elif probability > 0.4:
        st.info("Moderate probability. Lifestyle improvements suggested.")
    else:
        st.success("Healthy range detected.")

    # =====================
    # SAVE HISTORY
    # =====================
    record = {
        "Time": datetime.datetime.now(),
        "Glucose": glucose,
        "BMI": bmi,
        "Age": age,
        "Risk": risk_text
    }

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(record)

# =====================
# HISTORY PANEL
# =====================
if "history" in st.session_state:

    st.markdown("## 📜 Prediction History")
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)

    # DOWNLOAD REPORT
    csv = history_df.to_csv(index=False)
    st.download_button(
        "📥 Download Report",
        csv,
        "diabetes_report.csv",
        "text/csv"
    )

# =====================
# FOOTER
# =====================
st.markdown("---")
st.markdown("💙 Built with Machine Learning & Streamlit")
