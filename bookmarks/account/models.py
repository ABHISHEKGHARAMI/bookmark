from django.db import models
from django.conf import settings

# Create your models here.

# have to add more information along with django user model so we made addition model
# which will work one-to-one along with django user model

class Profile(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    date_of_birth = models.DateField(blank=True,null=True)
    
    image = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    
    
    def __str__(self):
        return f'Profile of {self.user.username}'
