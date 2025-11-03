from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from trips import views as trips_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # existing mapping(s)
    path('', include('trips.urls')),          # root -> trips
    path('trips/', include('trips.urls')),    # /trips/ -> trips

    # add this so /travel_site/ also shows trips
    path('travel_site/', include('trips.urls')),
    path('travel_site/', trips_views.project_home, name='project_home'),

    path('bookings/', include('bookings.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_short'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_short'),
]
