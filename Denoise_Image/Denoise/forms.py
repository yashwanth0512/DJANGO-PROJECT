from django import forms
from .models import Image
from .models import Hello

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
class HelloForm(forms.ModelForm):
    class Meta:
        model = Hello
        fields = ['first_name', 'last_name', 'email', 'phone']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email ID',
            'phone': 'Phone Number',
        }