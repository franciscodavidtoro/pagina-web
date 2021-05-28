
from django.urls import path
from .views import cont, prin
urlpatterns = [
    path('', prin, name='home'),
    path('contactos', cont, name='contactos')
]
