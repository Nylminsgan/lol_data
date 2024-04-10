import streamlit as st
import pandas as pd
import requests as re

api_key = "RGAPI-a54832df-ff96-4069-87ca-e3a2089c0333"
player = []


def get_user_by_puuid(puuid):
    return re.get("https://europe.api.riotgames.com" + "/riot/account/v1/accounts/by-puuid/" + puuid + '?api_key=' + api_key).json()


def get_user(user):
    name, tag = user.strip().split("#")
    account_api = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + name + '/' + tag + '?api_key=' + api_key
    user = re.get(account_api)
    if user.ok:
        return user.json()
    else:
        return "Name nicht gefunden"


def get_matches(acc, amount=20):
    games_api = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/' + acc["puuid"] + '/ids?' + 'queue=420' + '&start=0&count='+ str(amount) + '&api_key=' + api_key
    games = re.get(games_api)
    if games.ok:
        return games.json()
    else:
        return "Name nicht gefunden"


def get_match_data(match_id):
    match_data_req = "https://europe.api.riotgames.com/lol/match/v5/matches/" + match_id + '?api_key=' + api_key
    return re.get(match_data_req).json()


st.text("Hello World!")
username = st.text_input("Username#Tag")
if st.button("Analyze"):
    user = get_user(username)
    st.json(user)
    games = get_matches(user)
    st.json(games)
    game = get_match_data(games[0])
    for participant in game["metadata"]["participants"]:
        player[participant] = get_user_by_puuid(participant)["gameName"]
    st.text(player)
