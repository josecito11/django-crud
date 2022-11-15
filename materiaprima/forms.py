from django import forms
from .models import Produccin, materiaprima, Inventario, Entrada, Salida

class ProduccinForm(forms.ModelForm):
    class Meta:
        model = Produccin
        fields = ['producto', 'cantidad', 'fecha']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'})
        }

class materiaprimaForm(forms.ModelForm):
    class Meta:
        model = materiaprima
        fields = ['cantidad', 'proveedor', 'fecha']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'})
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['descripcion', 'stock', 'entrada', 'salida', 'precio_unitario', 'categoria']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}),
            'entrada': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}),
            'salida': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'})
        }

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['producto', 'cantidad', 'descripcion', 'fecha']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'})
        }

class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ['producto', 'cantidad', 'descripcion', 'fecha']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'})
        }