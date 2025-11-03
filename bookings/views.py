from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from trips.models import Trip
from .models import Booking

@login_required
def create_booking(request):
    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        seats = int(request.POST.get('seats', 1))
        trip = get_object_or_404(Trip, id=trip_id)
        if trip.available_seats >= seats:
            Booking.objects.create(user=request.user, trip=trip, seats_booked=seats)
            trip.available_seats -= seats
            trip.save()
            return redirect('bookings:my_bookings')
        else:
            return render(request, 'bookings/error.html', {'message':'Not enough seats.'})
    return redirect('trips:trip_list')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
