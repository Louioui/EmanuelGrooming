from django.urls import path
from .views import LoginView, SignupView, addDogView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('signup/', SignupView, name='signup'),
    path('add_dog/', addDogView, name='add_dog'),
]
