import streamlit as st
import pandas as pd

st.text("Hello World!")
username = st.text_input("Username + #")
st.form_submit_button('Login')

# Just add it after st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])
