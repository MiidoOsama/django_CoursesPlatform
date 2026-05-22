from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username',
            'required': 'required',
            'style': 'height: 50px; border-radius: 5px;'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
            'required': 'required',
            'style': 'height: 50px; border-radius: 5px;'
        })
    )


class UserRegesterationForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'style': 'height: 50px; border-radius: 5px;'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name != 'role':
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control',
                    'style': 'height: 50px; border-radius: 5px;'
                })
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create a strong password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat your password'})

