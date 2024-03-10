from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')  # Redirect back to the login page
    return render(request, 'login.html')
