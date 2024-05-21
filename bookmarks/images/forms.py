from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests

#here we go for the creation of the form

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','url','description']
        widgets = {
            'url' : forms.HiddenInput
        }
        
    # checking the url is valid or not extension of the image is valid or not
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.',1)[1].lower()
        
        if extension not in valid_extensions:
            raise forms.ValidationError('The url does not match with the extension given.')
        return url
    
    
    # forms provide the save method for the user to save the model
    def save(self,force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.',1)[1].lower()
        image_name = f'{name}.{extension}'
        
        # download the image from the given url
        response = requests.get(image_url)
        # go for the saving of the image
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image
        