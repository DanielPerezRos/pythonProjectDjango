# DJANGO EN PYCHARM COMMUNITY

1. Crear proyecto python
2. Ejecutar terminal 'pip install django'cd
3. Generar proyecto django:
...
   cd..
   django-admin startproject pythonProjectDjango pythonProjectDjango
   
...

Nota: cambiar pythonProjectDjango por el nombre asignado al proyecto python

4. Generar aplicación:
...
   cd pythonProjectDjango
   python manage.py startapp app
   
...

5. Crear migraciones
...
   python manage.py makemigrations
   
...

6. Ejecutar migraciones
...
   python manage.py migrate
   
...
   
7. Ejecutar aplicación
...
   python manage.py runserver
   
...

8. Añadir nombre app a archivo settings en la lista INSTALLED_APPS (moverlo a después del paso 4)
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]
...

9. Cambiar el lenguaje y la zona horaria en settings
...
LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'
...

10. Crear usuario para el panel de admin
...
    python manage.py createsuperuser
...
    
Nombre de usuario: root
Dirección de correo electrónico: ahhrrc@gmail.com
Password: admin

11. Arrancar el server con runserver y  Entrar en https://localhost:8000/admin

12. configuramos la BD mysql en settings

13. pip install mysqlclient

14. ejecutar las migraciones (makemigrations y migrate)


15. Creamos el usuario en mysql
---
python manage.py createsuperuser
---

16. Arrancar el server con runserver y  Entrar en https://localhost:8000/admin

# DESARROLLO CON DJANGO

17. CONFIGURAR LAS URLS en el archivo urls.py del proyecto:
---
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls'))
]
---

18. Creamos un archivo urls.py en la aplicación:
---
from django.urls import path
from . import views

urlpatterns = [
    path('holamundo', views.hola_mundo)
]
---
19. En el archivo views.py del aplicación creamos el contenido al que llama la url (mapeamos urls a vistas)
---
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo")
---

20. Probamos la url:
---
http://127.0.0.1:8000/app/holamundo
---

21. Creamos la carpeta templates dentro de la app y dentro creamos home.html