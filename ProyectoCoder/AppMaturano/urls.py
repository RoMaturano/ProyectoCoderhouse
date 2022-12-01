from django.urls import path
from AppMaturano import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.producto,name="producto"),
    path('carrito/', views.carrito,name="carrito"),
    path('busquedaProducto/', views.buscarproducto),
    path('buscar/', views.buscar),
]