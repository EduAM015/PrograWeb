# Panadería Lupita - Proyecto Django

Este proyecto convierte el sitio web estático de Panadería Lupita en una aplicación web Django.

## Instalación

1. Instala Python 3.8 o superior si aún no lo tienes.
2. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

3. Ejecuta las migraciones:

```
python manage.py migrate
```

4. Inicia el servidor de desarrollo:

```
python manage.py runserver
```

5. Visita http://127.0.0.1:8000/ en tu navegador.

## Estructura del proyecto

- `panaderia_lupita/` - Directorio principal del proyecto Django
- `panaderia/` - Aplicación principal que contiene las vistas y modelos
- `templates/` - Plantillas HTML
- `static/` - Archivos estáticos (CSS, JS, imágenes)