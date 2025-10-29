from django.shortcuts import render, get_object_or_404
from .models import Trip

def trip_list(request):
    trips = Trip.objects.order_by('start_date')
    return render(request, 'trips/trip_list.html', {'trips': trips})

def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'trips/trip_detail.html', {'trip': trip})
