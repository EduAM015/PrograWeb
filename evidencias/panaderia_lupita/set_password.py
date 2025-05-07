from django.contrib.auth.models import User

# Obtener el usuario admin
user = User.objects.get(username='admin')

# Establecer la contraseña
user.set_password('admin123')

# Guardar los cambios
user.save()

print("Contraseña establecida correctamente para el usuario admin")