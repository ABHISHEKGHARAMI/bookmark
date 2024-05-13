from django import forms

class LoginForms(forms.Form):
    
    # creating the login using the django form
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    