from django.shortcuts import render
from .models import producto
# Create your views here.
def tienda(request):
    prod = producto.objects.all()
    return render(request, "tienda.html", {"prod": prod})