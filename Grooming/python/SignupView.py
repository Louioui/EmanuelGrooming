from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
