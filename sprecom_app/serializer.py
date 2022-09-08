from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['spre_url','number_of_recs']