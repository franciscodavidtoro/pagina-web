
from django.urls import path
from .views import * 
urlpatterns = [
    path('tienda', tienda, name='tienda'),
    path('producto/<int:ids>', verproducto,name='productos'),#<int:ids> hace referencia a una variable de tipo entero con nombre'ids' en la uvicacion de la url para hacerla dinamica
    path("compra/<int:ids>",correo, name="compra"),
    path("error",error, name="error"),
    path("ok",ok, name="ok"),
    path("categoria/<int:ids>",categorias, name="categoria"),
]