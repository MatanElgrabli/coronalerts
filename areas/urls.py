from django.urls import path

from . import views

app_name = 'areas'
urlpatterns = [
    path('', views.index, name='index'),
]
