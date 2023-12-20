from django import forms
from .views import *
from .models import Bike

class ClientRegistrationForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    birthday = forms.DateField()
    phone = forms.IntegerField()
    password = forms.CharField(max_length=20)
    confirm_password = forms.CharField(max_length=20)
    
class ClientLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    
class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('make','model', 'description', 'image', 'price','engine','torque','weight')
        
class MessageForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':3,'cols':40}))


class contactform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'row':3,'col':30}))

