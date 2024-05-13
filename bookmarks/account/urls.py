# view for the account app
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# pattern for the user login
urlpatterns = [
    #path('login/',views.user_login,name='login'),
    # time for using the django auth views
    path('login/',auth_views.LoginViews.as_views(),name="login"),
    path('logout/',auth_views.LogoutViews.as_views(),name="logout"),
]