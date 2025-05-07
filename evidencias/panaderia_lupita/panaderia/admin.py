from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'fecha_envio')
    search_fields = ('nombre', 'correo', 'mensaje')
    list_filter = ('fecha_envio',)
    readonly_fields = ('fecha_envio',)