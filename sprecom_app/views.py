from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from . models import *
from . serializer import *
from rest_framework.response import Response
from django.http import HttpResponse
from . import scripts
from . forms import urlform
import pandas as pd
from . import final_model
from pathlib import Path
import os

#dirname = os.path.dirname(os.path.abspath("__file__"))
song_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data\\allsong_data.csv"))
complete_feature_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data\\complete_feature.csv"))

# def index(request):
#     return render(request,'index.html')

# def form(request):
#     if request.method == 'POST':
#         form = urlform(request.POST)
#         if form.is_valid():
#             playlist_url = form.cleaned_data['playlist_url']
#             number_of_recs = form.cleaned_data['number_of_recs']
#             #print(playlist_url)

#             df = scripts.extract(playlist_url)
#             #print(df)
#             top40songs = final_model.recommend_from_playlist(song_df,complete_feature_df,df)
#             #print('\n',top40songs[:number_of_recs])
#             my_songs = []
#             for i in range(number_of_recs):
#                 #my_songs.append([str(top40songs.iloc[i,1]) + ' - '+ '"'+str(top40songs.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(top40songs.iloc[i,-6]).split("/")[-1]])
#                 #my_songs.append([str(top40songs.iloc[i,-6]).split("/")[-1] + ' - '+ '"'+str(top40songs.iloc[i,4])+'"', "https://open.spotify.com/track/"+ str(top40songs.iloc[i,1])])
#                 my_songs.append([str(top40songs.iloc[i,0]) + '-' +str(top40songs.iloc[i,2]) , "https://open.spotify.com/track/"+ str(top40songs.iloc[i,1])])
#             # for i in my_songs:
#             #     print(i)
#             return render(request,'results.html',{'songs':my_songs})

#     # URL = request.GET
#     # df = scripts.extract(URL)
#     form = urlform()
#     return render(request,'form.html',{'form':form})

class UserViewSet(APIView):
    def post(self, request, format="json"):
        print(request)
        playlist_url = request.data['playlist_url']
        number_of_recs = int(request.data['number_of_recs'])
        #print(playlist_url)
        try:
            df = scripts.extract(playlist_url)
            #print(df)
            top40songs = final_model.recommend_from_playlist(song_df,complete_feature_df,df)
            #print('\n',top40songs[:number_of_recs])
            my_songs = []
            for i in range(number_of_recs):
                my_songs.append([str(top40songs.iloc[i,0]) + '-' +str(top40songs.iloc[i,2]) , "https://open.spotify.com/track/"+ str(top40songs.iloc[i,1])],top40songs.iloc[i,-1])
            return Response({'status': 'OK', 'data': my_songs}, status=status.HTTP_200_OK)
        except: 
            return Response({'status': 'KO', 'remark': 'Error encountered with the url. Please try again with a new url. Ensure that it is public.'}, status=status.HTTP_400_BAD_REQUEST)