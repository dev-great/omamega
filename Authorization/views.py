from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Authorization.models import CustomUser


def custom_login_view(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, username=email, password=password)
            print(user)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in.')
                # Replace with your desired redirect URL
                return redirect('core:index')
            else:
                # Add an error message if authentication fails
                messages.error(request, 'Invalid email or password')
        except KeyError:
            # Handle the case where 'email' or 'password' key is missing in the request
            messages.error(
                request, 'Missing email or password in the request.') 

    return render(request, 'registration/login.html')


def changePassword(request):
    return render(request, 'registration/change_password.html')
