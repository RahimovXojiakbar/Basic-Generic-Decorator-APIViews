from rest_framework.serializers import ModelSerializer
from . import models as md

class WeatherSerializer(ModelSerializer):
    class Meta:
        model = md.WeatherModel
        fields = '__all__'
        