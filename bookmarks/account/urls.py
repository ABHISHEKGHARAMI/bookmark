# view for the account app
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


# pattern for the user login
urlpatterns = [
    #path('login/',views.user_login,name='login'),
    # time for using the django auth views
    
 #   path('login/',auth_views.LoginView.as_view(),name='login'),
 #   path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    #  adding the password change for the user
 #   path('password-change/',auth_views.PasswordChangeView.as_view(),
 #        name='password_change'),
    
    # adding the password change done
 #   path('password-change/done/',
  #       auth_views.PasswordChangeDoneView.as_view(),
 #        name='password_change_done'),
    
    
    # resetting the password reset
  #  path('password-reset/',
   #      auth_views.PasswordResetView.as_view(),
   #      name='password_reset'),
    
    
   # path('password-reset/done/',
   #      auth_views.PasswordResetDoneView.as_view(),
  #       name='password_reset_done'),
    
   # path('password-reset/<uidb64>/<token>/',
   #      auth_views.PasswordResetConfirmView.as_view(),
  #       name='password_reset_confirm'),
    
  #  path('password-reset/complete/',
  #       auth_views.PasswordResetCompleteView.as_view(),
   #      name='password_reset_complete'),
     
     path('',include('django.contrib.auth.urls')),
    
    # adding the dashboard
     path('',views.dashboard,name='dashboard'),
    # password Abhi1998 pass Abhi1998@
    
    # have to add the new user registration for the registration
    
    path('register/',views.register,name="register"),
    
    path('edit/',views.edit,name="edit"),
    path('users/',views.user_list,name='user_list'),
    path('users/<username>/',views.user_detail,name='user_detail'),
]