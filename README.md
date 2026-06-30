# Multiple-Disease-Prediction-Using-Streamlit
# 🧠 Multiple Disease Prediction System using Machine Learning

This project is a **Machine Learning-based web application** that predicts multiple diseases using trained models. It helps users get early insights based on medical parameters and supports decision-making for further medical consultation.

---

## 🚀 Features

- Predicts multiple diseases in one application:
  - 🫀 Heart Disease Prediction
  - 🧬 Diabetes Prediction
  - 🧠 Parkinson’s Disease Prediction
- Simple and interactive UI built with **Streamlit**
- Trained ML models loaded for real-time prediction
- User-friendly input forms for medical parameters
- Fast and lightweight web app

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn 🤖
- Streamlit 🌐
- Pickle (for model saving/loading)

---

## 📂 Project Structure

multiple-disease-prediction/
│
├── models/
│ ├── heart_model.pkl
│ ├── diabetes_model.pkl
│ └── parkinsons_model.pkl
│
├── app.py
├── multiple_disease_prediction.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/your-username/multiple-disease-prediction.git

cd multiple-disease-prediction

### 2. Create virtual environment (optional but recommended)
python -m venv venv

venv\Scripts\activate   # Windows
### 3. Install dependencies
pip install -r requirements.txt

## ▶️ Run the Application
streamlit run app.py

Then open:

http://localhost:8501

## 📊 How It Works
User selects a disease prediction page

Enters medical parameters (e.g., glucose level, BP, etc.)

Trained ML model processes input

System returns prediction:
✅ Healthy / No disease
⚠️ Disease detected

## 📌 Example Inputs
## 📊 How It Works

The application provides prediction modules for three diseases:

### 🩸 Diabetes Prediction
Input Features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### ❤️ Heart Disease Prediction
Input Features:
- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate Achieved (thalach)
- Exercise-Induced Angina (exang)
- ST Depression (oldpeak)
- Slope
- Number of Major Vessels (ca)
- Thalassemia (thal)

### 🧠 Parkinson's Disease Prediction
Input Features:
- MDVP:Fo(Hz)
- MDVP:Fhi(Hz)
- MDVP:Flo(Hz)
- MDVP:Jitter(%)
- MDVP:Jitter(Abs)
- MDVP:RAP
- MDVP:PPQ
- Jitter:DDP
- MDVP:Shimmer
- MDVP:Shimmer(dB)
- Shimmer:APQ3
- Shimmer:APQ5
- MDVP:APQ
- Shimmer:DDA
- NHR
- HNR
- RPDE
- DFA
- Spread1
- Spread2
- D2
- PPE

After entering the required values, the corresponding trained machine learning model processes the inputs and predicts whether the disease is likely to be present.

## 📸 Output
The system displays:

Prediction result (Positive / Negative)

Risk status

Simple UI dashboard

## 📈 Future Improvements
Add more diseases (Cancer, Liver, Kidney)

Improve model accuracy

Deploy using AWS / Render / Streamlit Cloud

Add authentication system

Add medical report download feature
