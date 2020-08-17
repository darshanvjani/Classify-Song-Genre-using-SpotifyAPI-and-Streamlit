import requests
import urllib.parse
import pickle
import numpy as np

model = pickle.load(open('F:\Classify Song Genres from Audio Data\SVM_model','rb'))
transformer = pickle.load(open('F:\Classify Song Genres from Audio Data\Standardscaler','rb'))

class SpotifyClient():
    def __init__(self,oath_token):
        self.api_token=oath_token
        
    def search_song(self,track,artist):
        
        query = urllib.parse.quote(f'{artist} {track}')
        url = f'https://api.spotify.com/v1/search?q={query}&type=track'
        
        response = requests.get(
            url,
            headers = {
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {self.api_token}"
            }
        )
        
        response_json = response.json()
        
        results = response_json['tracks']['items']
        
        if results:
            self.song_id = results[0]['id']
            return 0
        else:
            return 1

    def extract_features(self):
        url_feature = f"https://api.spotify.com/v1/audio-features/{self.song_id}"
            
        response_features = requests.get(
            url_feature,
            headers = {
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {self.api_token}"
            }
        )

        self.response_features_json = response_features.json()
            
        if self.response_features_json:
            pass
        else:
            print("No feature found")
        return 0
        
    def feature_cleaning(self):
        feature_list = []
        temp_features = self.response_features_json
        
        for x in ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'tempo', 'valence']:
            feature_list.append(temp_features.get(x))
            
        self.feature_list = feature_list   
         
        #print(feature_list)    
        '''
         -> next step is feature normalization 
         -> loading the model 
         -> creating webpp using Streamlit
         -> deploying it on heroku
         -> Dockerising it
         
        '''
    def normalization(self):
        
       self.predict_this_value = transformer.transform(np.array(self.feature_list).reshape(1,-1))

    def prediction(self):
        
        return model.predict(self.predict_this_value)
             
'''obj_temp = SpotifyClient("BQCwmbk5qO1YUv0DW_7qtXHPsZj5XxWtpljLHSCCYlfiUXWmHGn_DNJis0UYlMTDyLEv2T0R7R6O9MXV3_HTdNuTaph9QbYg0JDiu_GG2a0km_eOv9UZ2m8Zj3fwpH4qsuonTuq08nMDIRdE83b5xfZd2HMlpaU")
obj_temp.search_song(track="Circles",artist="Post Malone")
obj_temp.extract_features()        
obj_temp.feature_cleaning()
obj_temp.normalization()
obj_temp.prediction()'''
# acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence
