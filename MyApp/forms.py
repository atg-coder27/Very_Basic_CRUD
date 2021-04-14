from django import forms 
from .models import User 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username' : 'Enter Name', 
            'email':'Enter Email',
            'password':'Enter Password',
            }
        widgets = {
            'password': forms.PasswordInput(),
        }
