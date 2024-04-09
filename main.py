import streamlit as st
import pandas as pd

st.text("Hello World!")
username = st.text_area("Username + #")

# Just add it after st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])
