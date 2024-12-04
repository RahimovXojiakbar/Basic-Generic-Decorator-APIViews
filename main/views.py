# from rest_framework.views import APIView -----------------> Basic API View
# from rest_framework.generics import ListAPIView --------------> Generic API View
# from rest_framework.decorators import api_view ------------------> Decorator API View



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView
from rest_framework.decorators import api_view
from . import serializers as ser
from . import models as md
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


class WeatherAPIView(APIView):
    def get(self, request, format=None):
        model = md.WeatherModel.objects.all()
        serializer = ser.WeatherSerializer(model, many=True)
        
        return Response(serializer.data)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Pagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 100

class WeatherGenericView(ListAPIView):
    queryset = md.WeatherModel.objects.all()
    serializer_class = ser.WeatherSerializer
    pagination_class = Pagination

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


@api_view(['GET'])
def weatherview(request):
    model = md.WeatherModel.objects.all()
    serializer = ser.WeatherSerializer(model, many=True).data

    return Response(serializer)









