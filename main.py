import streamlit as st
import pandas as pd

st.text("Hello World!")

# Just add it after st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])
print(a)
