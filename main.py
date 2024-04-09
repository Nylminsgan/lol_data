import streamlit as st
import pandas as pd

st.text("Hello World!")
with st.form(key='my_form'):
   username = st.text_input("Username#Tag")
   st.form_submit_button('analyze')

# Just add it after st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])
