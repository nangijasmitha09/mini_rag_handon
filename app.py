import streamlit as st

st.title("Hello Streamlit")

st.write("My Streamlit app is working!")

name = st.text_input("Enter your name")

if st.button("Test"):
    st.success(f"Hello {name}!")