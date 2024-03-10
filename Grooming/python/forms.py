from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class DogDetailsForm(forms.Form):
    dog_name = forms.CharField(max_length=50)
    breed = forms.CharField(max_length=50)
    age = forms.IntegerField()
