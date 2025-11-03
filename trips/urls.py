from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('trip/<int:pk>/', views.trip_detail, name='trip_detail'),
]
