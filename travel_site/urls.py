from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('trips.urls')),
    path('trips/', include('trips.urls')),
    path('bookings/', include('bookings.urls')),

    # existing auth routes (keeps /accounts/login/ as well)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # new short routes -> also available at /login/ and /logout/
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_short'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_short'),
]
