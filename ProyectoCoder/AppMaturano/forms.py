from django import forms 

class ProductoFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    fecha_de_ingreso=forms.CharField()
    