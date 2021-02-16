from django import forms
from django.forms import FileInput
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image_file', 'image_url')


class UserForm(forms.Form):
    weight = forms.IntegerField()
    height = forms.IntegerField()