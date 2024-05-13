# view for the account app
from django.urls import path
from . import views


# pattern for the user login
urlpatterns = [
    path('login/',views.user_login,name='login'),
]