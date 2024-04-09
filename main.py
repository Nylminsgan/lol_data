import streamlit as st
import pandas as pd
import requests as re

api_key = "RGAPI-a54832df-ff96-4069-87ca-e3a2089c0333"

def get_user_data(user):
    name, tag = user.strip().split("#")
    account_api = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + name + '/' + tag + '?api_key=' + api_key
    account_details = re.get(account_api).json()["puuid"]
    st.text("Eingegebener name: " + name + "#" + tag)
    st.text(account_details)
    pass


st.text("Hello World!")
username = st.text_input("Username#Tag")
if st.button("Analyze"):
    get_user_data(username)



