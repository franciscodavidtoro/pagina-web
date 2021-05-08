
from django.urls import path
from .views import prin
urlpatterns = [
    path('', prin, name='home')
]
