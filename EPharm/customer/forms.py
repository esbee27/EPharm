from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product
from django.forms import EmailInput, TextInput 

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=200,  help_text='Required')
    firstname = forms.CharField(max_length=200, help_text='Required')
    lastname = forms.CharField(max_length=200, help_text='Required')
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_no = forms.CharField(max_length=200, help_text='Required')
    birthday = forms.DateField(help_text='Required')
    state = forms.CharField(max_length=200, help_text='Required')


    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'phone_no', 
                  'birthday', 'state', 'password1', 'password2', 'username')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']