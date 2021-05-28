from django.shortcuts import render

# Create your views here.
def prin(request):
    return render(request, 'principal.html')

def cont(request):
    return render(request, 'contactos.html')