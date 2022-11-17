from cProfile import label
from django import forms


class RegistrationForm( forms.Form ):
    username   = forms.CharField ( label='User name', max_length=50 )
    first_name = forms.CharField ( label='First name', max_length=50 )
    last_name  = forms.CharField ( label='Last name', max_length=50, required=False )
    email      = forms.EmailField( label='Email', max_length=320 )
    password   = forms.CharField ( label='Password', max_length=128, widget=forms.PasswordInput(  ) )