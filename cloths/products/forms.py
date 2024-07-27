from django import forms
from .models import Men, Women
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm 

class MenForm(forms.ModelForm):
    class Meta:
        model = Men
        fields = ['Style_Type', 'Product_Type', 'price', 'size', 'image']

class WomenForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ['style_type', 'product_type', 'price', 'size', 'image']


class RegistrationForm(UserCreationForm):  
    email = forms.EmailField(required=True)  

    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')