from django.urls import path

from . import views # new

urlpatterns = [
    path('upload/', views.image_upload_view, name='upload'),
    path('', views.home_view, name='home'),
    path(r'^(?P<pk>\d+)', views.image_resizing, name='image_resizing'),
]