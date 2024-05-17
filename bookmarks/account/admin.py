from django.contrib import admin
from .models import Profile

# Register your models here.

# registering the model for the user
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']
    