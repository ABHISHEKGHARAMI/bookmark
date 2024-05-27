from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .forms import LoginForms , UserRegistrationForm , UserEditForm , ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contact



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


# using the decorators
@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {
            'section' : 'dashboard'
        }
    )
    
    
# register  view for new user
def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        # checking the user form is valid
        if user_form.is_valid() :
            # creating the user but dont commit the user
            #print(user_form)
            new_user = user_form.save(commit=False)
            # check the password for the user
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            
            # saving the password
            new_user.save()
            
            # after creating the new user have to create the profile
            Profile.objects.create(user=new_user)
            
            
            return render(
                request,
                "account/register_done.html",
                {
                    'new_user' : new_user
                }
            )
    else:
        user_form = UserRegistrationForm()
        
    # render the registration form
    return render(request,
                  "account/register.html",
                  {
                      'user_form' : user_form
                  })
    
    
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance = request.user,
                                 data = request.POST)
        profile_form = ProfileEditForm(instance = request.user.profile,
                                     data = request.POST,
                                     files = request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile Updated successfully.")
        else:
            messages.error(request,"Error updating the Profile.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
        
    return render(
        request,
        'account/edit.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )
    
@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(
        request,
        'account/user/list.html',
        {
            'section' : 'people',
            'users' : users
        }
    )
    
    
@login_required
def user_detail(request,username):
    user = get_object_or_404(User,username=username,is_active=True)
    
    
    return render(
        request,
        'account/user/detail.html',
        {
            'section':'people',
            'user' : user
        }
    )
    