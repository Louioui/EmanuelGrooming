from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, DogDetailsForm
from .models import User, Customer, Dog

def index(request):
    return render(request, 'index.html')

def user_login(request):
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
            return redirect('index')
    return render(request, 'index.html')

@login_required
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def add_dog(request):
    if request.method == 'POST':
        form = DogDetailsForm(request.POST)
        if form.is_valid():
            dog_name = form.cleaned_data['dog_name']
            breed = form.cleaned_data['breed']
            age = form.cleaned_data['age']
            customer, created = Customer.objects.get_or_create(user=request.user)
            dog = Dog.objects.create(customer=customer, dog_name=dog_name, breed=breed, age=age)
            messages.success(request, 'Dog added successfully!')
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
            return redirect('index')
    else:
        form = DogDetailsForm()
    return render(request, 'add_dog.html', {'form': form})

