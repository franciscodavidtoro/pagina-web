from django.shortcuts import render, redirect
from .models import producto
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.


def tienda(request):
    prod = producto.objects.all()
    return render(request, "tienda.html", {"prod": prod})


def verproducto(request, ids): # obtengo la bariable ids para crear la urldinamica
    obj = producto.objects.get(id=ids) # combienro ids en la id de la bace de datos
    context = {
        "prod": obj
    }
    return render(request, "productos.html", context)


def contact(request, ids):
    if request.method == 'GET': # get es obtener los datos sino se asume que se envian datos al server
        obj = producto.objects.get(id=ids)
        
        form = ContactForm()
        return render(request, "contacto.html", {'form': form, "prod": obj})
    else:
        obj = producto.objects.get(id=ids)
        form = ContactForm(request.POST)
        if form.is_valid():
            sp=' '
            info_prod='|| '+'Producto:'+obj.nombre+sp+'Precio:'+str(obj.precio)+'$ '+'ID:'+str(obj.id)
            info_clien='Nombre del cliente:'+form.cleaned_data['nombre']+sp+'Numero del cliente:'+str(form.cleaned_data['numero_celular'])
            from_email = form.cleaned_data['email']
            message = info_clien+sp+'Mensage:'+form.cleaned_data['mensage']+sp+info_prod
            subject = 'nuevo mensaje'
            try:
                send_mail(subject, message, from_email, [
                          'davidfranciscotoro@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/ok')
        else:
            return redirect('/error')        

def error(request):
    return render(request, 'error.html')

def ok(request):
    return render(request, 'ok.html')