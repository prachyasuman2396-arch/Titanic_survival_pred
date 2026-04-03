import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Titanic Survival Predictor",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000/predict"

st.sidebar.title("Titanic App")
option = st.sidebar.radio(
    "Navigate",
    ["Prediction", "Insights"]
)

if option == "Prediction":

    st.title("Titanic Survival Prediction")
    st.markdown("Predict whether a passenger would survive the Titanic disaster")
    st.markdown("---")

    st.subheader("Passenger Details")

    col1, col2 = st.columns(2)

    with col1:
        Pclass = st.selectbox("Passenger Class", [1, 2, 3])
        Sex = st.selectbox("Gender", ["male", "female"])
        Age = st.slider("Age", 0, 100, 25)
        Fare = st.number_input("Fare", min_value=0.0, value=32.0)

    with col2:
        SibSp = st.number_input("Siblings/Spouses", min_value=0, max_value=10, value=0)
        Parch = st.number_input("Parents/Children", min_value=0, max_value=10, value=0)
        Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])
        Cabin = st.text_input("Cabin (optional)", "")

    Name = st.text_input("Passenger Name", "Braund, Mr. Owen Harris")

    st.markdown("---")

    if st.button("Predict Survival"):

        payload = {
            "Pclass": Pclass,
            "Name": Name,
            "Sex": Sex,
            "Age": Age,
            "SibSp": SibSp,
            "Parch": Parch,
            "Fare": Fare,
            "Embarked": Embarked,
            "Cabin": Cabin if Cabin != "" else None
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()

                survived = result["survived"]
                prob = result["survival_probability"]

                st.markdown("Prediction Result")

                if survived == 1:
                    st.success(f"Survived (Probability: {prob:.2f})")
                else:
                    st.error(f"Did Not Survive (Probability: {prob:.2f})")

                st.progress(int(prob * 100))

            else:
                st.error("API Error. Check FastAPI server.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

elif option == "Insights":

    st.title("Titanic Data Insights")
    st.markdown("Insights derived from EDA")
    st.markdown("---")

    st.subheader("Gender Impact")
    st.write("""
    Females had significantly higher survival (~74%)
    Males had very low survival (~19%)
    """)

    st.subheader("Passenger Class")
    st.write("""
    1st Class: Highest survival
    2nd Class: Moderate survival
    3rd Class: Lowest survival
    """)

    st.subheader("Age")
    st.write("""
    Children had higher survival
    Adults moderate
    Elderly lower survival
    """)

    st.subheader("Family Size")
    st.write("""
    Small families survived more
    Large families struggled
    """)

    st.subheader("Fare")
    st.write("""
    Higher fare leads to higher survival
    """)

    st.markdown("---")

    st.subheader("Visual Validation")

    data = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Survival Rate": [0.19, 0.74]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Gender"], data["Survival Rate"])
    ax.set_ylabel("Survival Rate")

    st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<center>Built with using FastAPI + Streamlit</center>",
    unsafe_allow_html=True
)