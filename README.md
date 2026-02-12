🧠 Diabetes Prediction Web App

A Machine Learning powered web application that predicts the risk of diabetes based on medical parameters. This project demonstrates end-to-end ML deployment including model training, API development, UI design, and cloud deployment.

🚀 Live Demo

👉 (Add your Streamlit deployed link here once deployed)

📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction helps in preventive healthcare and lifestyle management.

This application uses a Random Forest Machine Learning model to predict whether a person is likely to have diabetes based on health indicators such as glucose level, BMI, age, insulin level, etc.

🏗️ System Architecture
User Interface (Streamlit UI)
        ↓
Flask Prediction API
        ↓
Machine Learning Model (Random Forest)
        ↓
Prediction Result Display

✨ Features

✅ Interactive modern UI
✅ Real-time diabetes risk prediction
✅ Machine Learning powered backend
✅ REST API integration
✅ Clean and responsive dashboard
✅ Easy deployment and scalability
✅ Beginner friendly architecture

🧪 Machine Learning Model
🔹 Algorithm Used

Random Forest Classifier

🔹 Dataset

PIMA Indian Diabetes Dataset

🔹 Model Accuracy
Accuracy: 72%

🔹 Input Features
Feature	Description
Pregnancies	Number of pregnancies
Glucose	Blood glucose level
BloodPressure	Blood pressure value
SkinThickness	Skin fold thickness
Insulin	Insulin level
BMI	Body Mass Index
DiabetesPedigreeFunction	Genetic diabetes likelihood
Age	Age of patient
🖥️ Tech Stack
🔹 Frontend

Streamlit

🔹 Backend

Flask

REST API

🔹 Machine Learning

Scikit-learn

Pandas

NumPy

🔹 Deployment

Streamlit Cloud

GitHub

📂 Project Structure
Diabetes-Prediction-App
│
├── app.py                # Flask API backend
├── ui.py                 # Streamlit UI frontend
├── diabetes_model.pkl    # Trained ML model
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/Diabetes-Prediction-App.git
cd Diabetes-Prediction-App

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend API
python app.py

4️⃣ Run UI Application
streamlit run ui.py

📡 API Endpoint
POST /predict
Request Body (JSON)
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 30,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 35
}

Response
{
  "prediction": "Diabetic"
}

📊 Future Improvements

🔹 Add patient history database
🔹 Integrate SHAP AI explainability graphs
🔹 Add user authentication system
🔹 Deploy backend using Docker & AWS
🔹 Convert into mobile healthcare dashboard

🎓 Learning Outcomes

End-to-end Machine Learning workflow

REST API development

Streamlit UI design

Model deployment

GitHub project management

👨‍💻 Author

Arjya Banerjee


📜 License

This project is created for educational and research purposes.

⭐ If you like this project

Give it a ⭐ on GitHub!
