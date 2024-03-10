from .forms import DogDetailsForm
from .models import Dog
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_dog_view(request):
    if request.method == 'POST':
        form = DogDetailsForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.customer = request.user.customer  # Assuming customer is related to the logged-in user
            dog.save()
            messages.success(request, 'Dog added successfully!')
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
    else:
        form = DogDetailsForm()
    return render(request, 'add_dog.html', {'form': form})
