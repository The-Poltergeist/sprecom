from socket import fromshare
from django import forms

class urlform(forms.Form):
    playlist_url = forms.CharField(max_length=100,required=True)
    number_of_recs = forms.IntegerField(max_value=40)