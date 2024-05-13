from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .forms import LoginForms

# Create your views here.

# user login view
def user_login(request):
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd["username"],
                                password=cd["password"])
            
            if user is not None:
                if user.is_active:
                    return HttpResponse("Authenticate Successfully.")
                else:
                    return HttpResponse("Disabled Account.")
            else:
                return HttpResponse("Invalid Login.")
            
    else:
        form = LoginForms()
    return render(
        request,
        'account/login.html',
        {
            'form' : form
        }
    )
