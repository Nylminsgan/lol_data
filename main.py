import streamlit as st
import pandas as pd
import requests as re

api_key = "RGAPI-a54832df-ff96-4069-87ca-e3a2089c0333"

def get_match_data(match_id):
    match_data_req = "https://europe.api.riotgames.com/lol/match/v5/matches/" + match_id + '?api_key=' + api_key
    return re.get(match_data_req).json()
def get_user_match_data(user):
    name, tag = user.strip().split("#")
    account_api = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + name + '/' + tag + '?api_key=' + api_key
    acc = re.get(account_api)
    if acc.ok:
        acc = acc.json()
        st.text("Eingegebener name: " + acc["gameName"] + "#" + acc["tagLine"])
        games_api = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + acc["puuid"] + '/ids?' + 'queue=420' + '&start=0&count=20' + '&api_key=' + api_key
        games = re.get(games_api).json()
        return games
    else:
        st.text("Name nicht gefunden")
        return ""


st.text("Hello World!")
username = st.text_input("Username#Tag")
if st.button("Analyze"):
    games = get_user_match_data(username)
    match = get_match_data(games[0])
    st.text(match)



