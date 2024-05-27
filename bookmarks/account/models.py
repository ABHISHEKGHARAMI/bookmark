from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

# have to add more information along with django user model so we made addition model
# which will work one-to-one along with django user model

class Profile(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    date_of_birth = models.DateField(blank=True,null=True)
    
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    
    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    


# model for the contact
class Contact(models.Model):
    #here goes the property.
    user_form = models.ForeignKey('auth.User',
                                  related_name = 'rel_from_set',
                                  on_delete=models.CASCADE)
    
    user_to = models.ForeignKey('auth.User',
                                related_name = 'rel_to_set',
                                on_delete = models.CASCADE
                                )
    created = models.DateTimeField(auto_now_add=True)
    
    
    # meta class
    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']
    
    
    def __str__(self):
        return f"{self.user_form} follows {self.user_to}"
    
    
# added the following field to add user dynamically
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField(
                            'self',
                            through=Contact,
                            related_name='followers',
                            symmetrical=False
                        ))
