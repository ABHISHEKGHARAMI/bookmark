from django import forms
from .models import Image


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