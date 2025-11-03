# accounts/views.py
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def logout_and_show_message(request):
    """
    Accepts GET (or POST). Logs out the user then renders a simple logged_out page.
    """
    # perform logout 
    logout(request)
    return render(request, 'registration/logged_out.html')
