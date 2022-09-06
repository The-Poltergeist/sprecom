# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:24:15 2022

@author: enoch
"""

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
import re

#%%
# songs_df = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//allsong_data.csv")
# complete_feature_set = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//complete_feature.csv")
# playlist_df = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//test_playlist.csv")

#%%
#function to generate playlist feature
def generate_playlist_feature(complete_feature_set,playlist_df):
    #Find song features in playlist
    complete_feature_set_playlist = complete_feature_set[complete_feature_set['id'].isin(playlist_df['id'].values)]
    #Find songs features which are not in playlist
    complete_feature_set_nonplaylist = complete_feature_set[~complete_feature_set['id'].isin(playlist_df['id'].values)]
    complete_feature_set_playlist_final = complete_feature_set_playlist.drop(columns='id')
    return complete_feature_set_playlist_final.sum(axis=0),complete_feature_set_nonplaylist

#%%
#function to generate recom based on a particular playlist
def generate_playlist_recom(df,features,nonplaylist_features):
    nonplaylist_df = df[df['id'].isin(nonplaylist_features['id'].values)]
    #finding cosing similarity b/w playlist and complete song set
    nonplaylist_df['sim'] = cosine_similarity(nonplaylist_features.drop(columns='id',axis = 1).values,features.values.reshape(1,-1))[:,0]
    nonplaylist_df_top_40 = nonplaylist_df.sort_values('sim',ascending=False).head(40)
    
    return nonplaylist_df_top_40

#%%
# songs_df = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//allsong_data.csv")
# complete_feature_set = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//complete_feature.csv")
# playlist_df = pd.read_csv("C://Users//enoch//OneDrive//Desktop//Work//Spotify recommender//data//test_playlist.csv")


#%%
#Pipeline
def recommend_from_playlist(songs_df,complete_feature_set,playlist_df):
    
    complete_feature_set_playlist_vector,complete_feature_set_nonplaylist = generate_playlist_feature(complete_feature_set, playlist_df)
    
    top40 = generate_playlist_recom(songs_df, complete_feature_set_playlist_vector, complete_feature_set_nonplaylist)
    
    return top40


#%%

if '__name__'=='__main__':
    print(recommend_from_playlist()[:10])