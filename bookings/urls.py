from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'bookings'

urlpatterns = [
    # When user visits /bookings/ show their bookings 
    path('', views.my_bookings, name='index'),

    # existing routes
    path('create/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
]
