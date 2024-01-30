from dotenv import load_dotenv
import dotenv
import os
import base64
import requests
from requests import post
import json
from django.shortcuts import render, HttpResponse

class Call:
    
    def get_token():
        dotenv_file = os.path.join(".env")
        if os.path.isfile(dotenv_file):
            load_dotenv(dotenv_file)
            client_id = os.getenv("CLIENT_ID")
            client_secret = os.getenv("CLIENT_SECRET")
            
            auth_string = client_id + ":" + client_secret
            auth_bytes = auth_string.encode("utf-8")
            auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

            url = "https://accounts.spotify.com/api/token"
            headers = {
                "Authorization" : "Basic " + auth_base64,
                "Content-Type"  : "application/x-www-form-urlencoded"
            }

            data = {"grant_type" : "client_credentials"}
            result = post(url, headers = headers, data =data)
            json_result = json.loads(result.content)
            token = json_result["access_token"]
            return token
        else:
            return 0

    def get_song_details(song_name, access_token):
        search_url = "https://api.spotify.com/v1/search/"
        parameters_of_query_string = {
            'q': song_name,
            'type': 'track',
            'limit': 1 
        }
        headers = {'Authorization': f'Bearer {access_token}'}
        result = requests.get(search_url, parameters_of_query_string, headers=headers)
        
        if result.status_code == 200:
            track_details = result.json()
            t_id = track_details["tracks"]["items"][0]["id"]
            t_name = track_details["tracks"]["items"][0]["name"]
            artists = track_details["tracks"]["items"][0]["artists"]
            
            print(f"\n\n{t_id}\n<'{t_name}'> by <'{artists[0]['name']}'>")
            return t_id
        else:
            return None

    def get_features(track_id, access_token):
        
        # Preparing the request to send for audio features
        features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'
        headers = {'Authorization': f'Bearer {access_token}'}
        
        # Sending a request and getting a response
        response = requests.get(features_url, headers=headers)
        
        if response.status_code == 200:
            print("YOOOOOO")
            audio_features = response.json()
            print( audio_features)
        else:
            print("NOOOOOOOO")