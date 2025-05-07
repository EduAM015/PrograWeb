from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    """Formulario para el modelo Contacto con validaciones personalizadas."""
    
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu Nombre:', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Tu Número:', 'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Tu Correo:', 'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Tu mensaje', 'class': 'form-control'}),
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise forms.ValidationError("Ingresa un nombre válido.")
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^[0-9]{10}$', telefono):
            raise forms.ValidationError("El número de teléfono debe tener 10 dígitos.")
        return telefono
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return mensaje