from django.shortcuts import render
from django.template.context_processors import csrf
from django.urls import path

from .models import Image
from .forms import ImageForm, UserForm
from PIL import Image as Im


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(request, 'img_resizing/post.html', {'form': form, 'img_obj': img_obj})
            except ValueError:
                data = 1
                return render(request, 'img_resizing/post.html', {'form': form, 'data': data})
    else:
        form = ImageForm()
    return render(request, 'img_resizing/post.html', {'form': form})


def home_view(request):
    image = Image.objects.order_by('-id')
    return render(request, 'img_resizing/home.html', {'title': 'Главная страница', 'image': image})


def image_resizing(request, pk):
    image = Image.objects.get(pk=pk)
    submitbutton = request.POST.get("submit")

    weight = ''
    height = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        weight = form.cleaned_data.get("weight")
        height = form.cleaned_data.get("height")

    if weight and height:
        img = image.img_resizing()
    else:
        img = Im.open(image.image_file.path)

    context = {'form': form, 'height': height,
               'weight': weight, 'submitbutton': submitbutton, 'image': image, 'img': img}

    return render(request, 'img_resizing/img_settings.html', context)