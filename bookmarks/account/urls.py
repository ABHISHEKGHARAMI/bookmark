# view for the account app
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# pattern for the user login
urlpatterns = [
    #path('login/',views.user_login,name='login'),
    # time for using the django auth views
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    #  adding the password change for the user
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    
    # adding the password change done
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    
    # adding the dashboard
    path('',views.dashboard,name='dashboard'),
]