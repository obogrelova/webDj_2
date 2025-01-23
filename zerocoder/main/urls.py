from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newpage2', views.newpage2),
    path('newpage3', views.newpage3),
    path('newpage4', views.newpage4)
]