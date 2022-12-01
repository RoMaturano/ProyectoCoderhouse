from django.shortcuts import render
from django.http import HttpResponse
from AppMaturano.models import Producto
from django.core import serializers
from AppMaturano.forms import ProductoFormulario


# Create your views here.
def buscar(request):
    nombre_buscado=request.GET["nombre"]
    productos_todos = Producto.objects.filter(nombre=nombre_buscado)
    return render(request,"AppMaturano/resultadobusqueda.html", {"nombre":nombre_buscado, "precio":productos_todos})

def buscarproducto(request):
    return render(request,"AppMaturano/busquedaProducto.html")


def inicio(request):
    return render(request,"AppMaturano/inicio.html")

def producto (request):
    todos_productos = Producto.objects.all()
    return HttpResponse(serializers.serialize("json",todos_productos))


def carrito (request):
    if request.method == "POST":
 
            miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  productoos = Producto(nombre=informacion["nombre"], precio=informacion["precio"], fecha_de_ingreso=informacion["fecha_de_solicitud"])
                  productoos.save()
                  return render(request, "AppMaturano/inicio.html")
    else:
                   miFormulario = ProductoFormulario()
 
    return render(request, "AppMaturano/carrito.html", {"miFormulario": miFormulario})
    
    
    
    
    
