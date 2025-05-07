from django.db import models

class Contacto(models.Model):
   
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.fecha_envio.strftime('%d/%m/%Y')}"
    
    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-fecha_envio']