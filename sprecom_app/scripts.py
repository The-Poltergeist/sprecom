import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json 
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def extract(URL):
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    type1 = URL.split('/')[3]

    if type1=='album':
        album_id = URL.split('/')[4].split('?')[0]
        playlist_tracks_data = sp.album_tracks(album_id)
        playlist_tracks_id = []
        playlist_tracks_titles = []
        playlist_tracks_artists = []
        playlist_tracks_first_artists = []    

        for track in playlist_tracks_data['items']:
            playlist_tracks_id.append(track['id'])
            playlist_tracks_titles.append(track['name'])

            artist_list = []

            for artist in track['artists']:
                artist_list.append(artist['name'])

            playlist_tracks_artists.append(artist_list)
            playlist_tracks_first_artists.append(artist_list[0])

        features = sp.audio_features(playlist_tracks_id)
        features_df = pd.DataFrame(data=features, columns=features[0].keys())
        features_df['title'] = playlist_tracks_titles
        features_df['first_artist'] = playlist_tracks_first_artists
        features_df['all_artists'] = playlist_tracks_artists
        features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                                    'danceability', 'energy', 'key', 'loudness',
                                    'mode', 'acousticness', 'instrumentalness',
                                    'liveness', 'valence', 'tempo',
                                    'duration_ms', 'time_signature']]

    elif type1=='playlist':
        playlist_id = URL.split('/')[4].split('?')[0]
        playlist_tracks_data = sp.playlist_tracks(playlist_id)
        playlist_tracks_id = []
        playlist_tracks_titles = []
        playlist_tracks_artists = []
        playlist_tracks_first_artists = []

        for track in playlist_tracks_data['items']:
            playlist_tracks_id.append(track['track']['id'])
            playlist_tracks_titles.append(track['track']['name'])

            artist_list = []

            for artist in track['track']['artists']:
                artist_list.append(artist['name'])
            
            playlist_tracks_artists.append(artist_list)
            playlist_tracks_first_artists.append(artist_list[0])

        features = sp.audio_features(playlist_tracks_id)
        features_df = pd.DataFrame(data=features, columns=features[0].keys())
        features_df['title'] = playlist_tracks_titles
        features_df['first_artist'] = playlist_tracks_first_artists
        features_df['all_artists'] = playlist_tracks_artists
        features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                                    'danceability', 'energy', 'key', 'loudness',
                                    'mode', 'acousticness', 'instrumentalness',
                                    'liveness', 'valence', 'tempo',
                                    'duration_ms', 'time_signature']]

    return features_df
