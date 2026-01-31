import streamlit as st

st.title("💪 AI Health Recommender")

name = st.text_input("Enter your name")

if name:
    st.header(f"Welcome {name} 💙")

weight = st.number_input("Enter weight (kg)")
height = st.number_input("Enter height (cm)")
age = st.number_input("Enter age")

if st.button("Calculate"):
    bmi = weight / ((height/100)**2)
    calories = 10*weight + 6.25*height - 5*age + 5

    st.success(f"BMI: {round(bmi,2)}")
    st.success(f"Calories Needed: {int(calories)} kcal")

