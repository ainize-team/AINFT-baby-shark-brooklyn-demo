import json
import requests
import streamlit as st

endpoint_url = 'https://develop-ainft-baby-shark-brooklyn-ainize-team.endpoint.ainize.ai'


twitter_id = st.sidebar.text_input("Twiter User ID")
twitter_update_btn = st.sidebar.button("Update")

chat_input = st.text_area("Input Text")
chat_btn = st.button("Chat")

chat_output = st.text("")


if twitter_update_btn:
    try:
        params = {
            'screen_name': twitter_id,
        }
        output = requests.get(f'{endpoint_url}/makeTwitterData', params=params)
    except Exception as e:
        output = f'Endpoint API Internal error occurs : {e}'


if chat_btn:
    try:
        params = {
            'text': chat_input,
            'twitter_id': twitter_id
        }
        response = requests.get(f'{endpoint_url}/chat', params=params)
        output = response.json()['message']
    except Exception as e:
        output = f'Endpoint API Internal error occurs : {e}'

    chat_output.text(output)
