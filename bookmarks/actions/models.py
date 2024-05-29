from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contenttypes.fields import GenericForeignkey

# Create your models here.
class Actions(models.Model):
    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             on_delete=models.CASCADE)
    
    verb = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering=['-created']