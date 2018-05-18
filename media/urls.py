
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('media', views.index, name='media'),
    path('upload', views.upload, name='upload')
]
