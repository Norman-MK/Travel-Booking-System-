from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import logout_and_show_message

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('trips.urls')),
    path('trips/', include('trips.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),


    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_short'),
    path('accounts/logout/', logout_and_show_message, name='logout'),
    path('logout/', logout_and_show_message, name='logout_short'),
]
