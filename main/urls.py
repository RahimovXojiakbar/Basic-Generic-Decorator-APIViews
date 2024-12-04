from django.urls import path
from . import views 
urlpatterns = [
    path('basic/', views.WeatherAPIView.as_view(), name='basic_url'),
    path('generic/', views.WeatherGenericView.as_view(), name='generic_url'),
    path('decorator/', views.weatherview, name='decorator_url'),
]