import streamlit as st
import pandas as pd


def get_user_data(user):
    print("get_user_data")
    pass


st.text("Hello World!")
username = st.text_input("Username#Tag")
if st.button("Analyze"):
    get_user_data(username)



