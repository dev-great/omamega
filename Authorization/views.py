from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
                if request.user.is_Landlord == False & request.user.is_Subscriber == True:
                    return redirect('core:subscriber')
                return redirect('core:index')
            else:
                # Add an error message if authentication fails
                messages.error(request, 'Invalid email or password')
        except KeyError:
            # Handle the case where 'email' or 'password' key is missing in the request
            messages.error(
                request, 'Missing email or password in the request.')

    return render(request, 'registration/login.html')


@login_required(login_url='Authorization:login')
def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, 'Incorrect current password.')
        elif new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
        else:
            # Update the password
            user.set_password(new_password1)
            user.save()

            # Update the session auth hash
            update_session_auth_hash(request, user)

            messages.success(
                request, 'Your password was successfully updated!')
            # Replace with the actual name of your password change done view
            return HttpResponseRedirect('/success/')

    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
    }
    context = {
        'user_details': user_details,
    }
    return render(request, 'registration/change_password.html', context)
