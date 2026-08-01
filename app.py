import streamlit as st
import pandas as pd
import joblib
import time

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)


st.markdown("""
<style>

.main{
    background: linear-gradient(to right,#eef2ff,#f8fafc);
}

h1{
    color:#E63946;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    background:#E63946;
    color:white;
    font-size:20px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#C1121F;
}

.block{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.12);
}

.result-good{
    padding:25px;
    border-radius:12px;
    background:#d1fae5;
    color:#065f46;
    font-size:28px;
    text-align:center;
    font-weight:bold;
}

.result-bad{
    padding:25px;
    border-radius:12px;
    background:#fee2e2;
    color:#991b1b;
    font-size:28px;
    text-align:center;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


model = joblib.load("knn_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")


st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/833/833472.png",
    width=120
)

st.sidebar.title("Heart Disease Predictor")

st.sidebar.info("""
This application predicts the likelihood of heart disease using a trained KNN Machine Learning model.

**Developer**
Omkar
""")



st.title("❤️ Heart Disease Prediction")

st.markdown(
"""
<center>
Enter your medical information below and click <b>Predict</b>.
</center>
""",
unsafe_allow_html=True)

st.write("")



col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="block">', unsafe_allow_html=True)

    age = st.slider("Age",18,100,40)

    sex = st.selectbox(
        "Gender",
        ["M","F"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA","NAP","TA","ASY"]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        80,200,120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        70,600,200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar >120",
        [0,1]
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown('<div class="block">', unsafe_allow_html=True)

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal","ST","LVH"]
    )

    max_hr = st.slider(
        "Maximum Heart Rate",
        60,220,150
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        ["Y","N"]
    )

    oldpeak = st.slider(
        "Oldpeak",
        0.0,6.0,1.0
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Up","Flat","Down"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")



if st.button("❤️ Predict Heart Disease Risk"):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    with st.spinner("Analyzing your health..."):
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)

    prediction = model.predict(scaled_input)[0]

    st.write("")

    if prediction == 1:

        st.markdown("""
        <div class='result-bad'>
        ⚠️ HIGH RISK OF HEART DISEASE
        </div>
        """, unsafe_allow_html=True)

        st.warning("""
Please consult a cardiologist for further diagnosis.

Maintain:

• Healthy diet

• Regular exercise

• Blood pressure monitoring

• Stress management

• Avoid smoking
""")

    else:

        st.markdown("""
        <div class='result-good'>
        ✅ LOW RISK OF HEART DISEASE
        </div>
        """, unsafe_allow_html=True)

        st.success("""
Keep maintaining a healthy lifestyle.

✔ Balanced diet

✔ Exercise

✔ Regular health checkups

✔ Good sleep

✔ Stay hydrated
""")

st.write("---")

st.caption("Developed by Omkar ❤️ | Machine Learning Heart Disease Prediction")
