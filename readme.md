# ❤️ Heart Disease Prediction using Machine Learning

A web application built with **Streamlit** that predicts the likelihood of heart disease using a trained **K-Nearest Neighbors (KNN)** machine learning model.

## 🚀 Features

* User-friendly Streamlit interface
* Predicts heart disease risk from patient information
* Fast and lightweight KNN model
* Instant prediction results
* Easy to deploy on Streamlit Community Cloud

---

## 📂 Project Structure

```text
HeartDiseasePrediction/
│── app.py
│── knn_heart_model.pkl
│── requirements.txt
│── runtime.txt
│── README.md
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Input Features

The model predicts heart disease using the following medical parameters:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* Slope of ST Segment
* Number of Major Vessels
* Thalassemia

---

## 🎯 Prediction Output

The application provides one of the following results:

* **Low Risk / No Heart Disease Detected**
* **High Risk / Heart Disease Detected**

> **Disclaimer:** This application is intended for educational and research purposes only. It is **not** a substitute for professional medical diagnosis or advice.

---

## 🌐 Deployment

This application can be deployed easily using **Streamlit Community Cloud**.

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app.
4. Select your GitHub repository.
5. Deploy the application.

---

## 📸 Screenshot

Add a screenshot of your application here.

```
assets/app_screenshot.png
```

---

## 👨‍💻 Author

**Omkar Chavan**

B.Tech CSE Student | Machine Learning Enthusiast

---

## 📄 License

This project is licensed under the MIT License.
