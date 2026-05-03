import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Student Mark Predictor")

hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance")
marks = st.number_input("Previous Marks")

if st.button("Predict"):
    result = model.predict([[hours, attendance, marks]])
    st.write(result)