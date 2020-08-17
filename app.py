import streamlit as st
import numpy as np
import pandas as pd
import time
from Auth import client_Auth
from oath_searchsongs import SpotifyClient

# Client ID: 5e5b17cbade949d7b149c0a5c9061b98
# Client Secret Key: d4c01f8e64074565903ce95119582f77

st.title("Classify Song Genres from Spotify!")
st.text("")
st.text("")

#getting Otoken
aoth = client_Auth()
Auth_code = aoth.token_request()

song_name = st.text_input(label="Name Of Song:")
artist_name = st.text_input(label="Name of Artist:")



if st.button("Classifying the Genre..."):
    with st.spinner("Predicting..."):
        time.sleep(5)
    obj = SpotifyClient(Auth_code)
    temp = obj.search_song(track = song_name, artist = artist_name)
    if temp == 0:
        obj.extract_features()        
        obj.feature_cleaning()
        obj.normalization()
        predicted_value = obj.prediction()
        print(predicted_value)
        if predicted_value == 1:
            st.text("ROCK")
        else:
            st.text("HIP-HOP")    
    else:
        st.text("NO SUCH SONG FOUND!")