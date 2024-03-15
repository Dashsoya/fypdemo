from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth import get_user_model
import random


# Create your views here.
def login_view(request):

   
    return render(request, 'login.html')

def loginauth(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'patient':
                return redirect('patienthome')
            elif user.role == 'doctor':
                return redirect('doctorhome')
            elif user.role == 'admin':
                return redirect('adminhome')
            else:
                return HttpResponse('Invalid1 credentials')
        
        else:
            return HttpResponse('Invalid credentials')

def patienthome_view(request):
    return render(request, 'patienthome.html')

def doctorhome_view(request):
    return render(request, 'doctorhome.html')

def adminhome_view(request):
    return render(request, 'adminhome.html')

def logoutbye(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login_view')

def accdetails(request):
    # Get the current user
    user = request.user

    # Pass the user object to the template context
    context = {
        'user': user,
    }
    return render(request, 'details.html', context)

@login_required
def updatedetails(request):
    if request.method == 'POST':
        
        user = request.user
        user.username = request.POST.get('newUsername')
        user.email = request.POST.get('newEmail')
        user.save()

        messages.success(request, "Details updated successfully!")
        return redirect('accdetails')  # Redirect to the user details page
    else:
        return render(request, 'update_details.html')  # Render the update details form
    

def list_users(request):
    # Fetch all users from the custom user model
    users = CustomUser.objects.all()

    # Pass the users data to the template
    return render(request, 'user_list.html', {'users': users})

def delete_user(request, account_id):
    User = get_user_model()
    try:
        # Fetch the user to be deleted
        user = User.objects.get(pk=account_id)
        # Delete the user
        user.delete()
        messages.success(request, f"User {user.username} has been deleted successfully!")
    except User.DoesNotExist:
        messages.error(request, "User does not exist!")
    
    # Redirect to the list of users after deletion
    return redirect('list_users')