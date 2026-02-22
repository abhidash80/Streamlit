import streamlit as st
import pandas as pd
import random

st.title("Streamlit Text Input")


name= st.text_input("Enter your name")
age=st.slider("Select your age:", 0,100,25)
st.write(f"Your age is {age}.")

options = ["Python", "Javascript", "C++", "Go"]
choice = st.selectbox(f"Choose your favorite coding lang:",options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")


names = ["Amit", "Rahul", "Sneha", "Priya", "Vikram", "Neha", "Arjun", "Kiran", "Rohit", "Anjali"]
cities = ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Delhi", "Pune", "Kolkata"]

data = {
    "Name": [random.choice(names) for _ in range(10)],
    "Age": [random.randint(20, 45) for _ in range(10)],
    "City": [random.choice(cities) for _ in range(10)]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)
