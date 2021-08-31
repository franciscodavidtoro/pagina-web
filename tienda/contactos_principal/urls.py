
from django.urls import path
from .views import cont, prin, acer
urlpatterns = [
    path('', prin, name='home'),
    path('contactos', cont, name='contactos'),
    path('nosotros', acer, name='nosotros'),
]
