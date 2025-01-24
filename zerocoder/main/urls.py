from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newpage2', views.newpage2, name='page2'),
    path('newpage3', views.newpage3, name='page3'),
    path('newpage4', views.newpage4, name='page4')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)