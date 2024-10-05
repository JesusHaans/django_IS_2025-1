# django_IS_2025-1
repositorio para ver los temas relacionados con Django en la materia de Ingeniería de Software de la facultad de ciencias de la UNAM.


# Clase 1 03/10/2025

## Antes de empezar

### ¿Qué es Django?
Es un framework de desarrollo web de código abierto, escrito en Python, que sigue el patrón de diseño Modelo-Vista-Template (MVT).

#### Ventajas
- facilidad de uso
- permite crear algo desde 0 a algo usable en poco tiempo

#### Algunos Ejemplos
almenos en sus primeras versiones:

- Instagram
- Spotify

Para empezar debemos entender que so los entornos virtuales y como instalarlos. Ya que nos ayudan a tener paquetes con versiones especificas para cada proyecto.

## Entornos Virtuales
Para crear un entorno virtual en python se utiliza el siguiente comando:

```bash
python -m venv path/nombre_del_entorno
```
### buenas practicas
- crear un archivo `.gitignore` para ignorar los archivos de entorno virtual
- crear un archivo `requirements.txt` para guardar las dependencias del proyecto
- el nombre del entorno virtual debe ser `.venv`
- el entorno virtual debe estar en la carpeta raiz del proyecto

### Activar entorno virtual
En Mac y Linux
```bash
source .venv/bin/activate
```
En Windows
```bash
.venv\Scripts\activate
```
Una vez activado el entorno virtual, el nombre del entorno virtual aparecerá en la terminal.

Ya teniendo el entorno virtual activado, podemos instalar las dependencias del proyecto (una de esas es Django).

### desactivar entorno virtual
En Mac, Linux y Windows
```bash
deactivate
```


## Instalación de Django

Una vez que tenemos el entorno virtual activado, podemos instalar Django en su ultima version con el siguiente comando:

```bash
pip install django
```

si queremos instalar una version especifica de Django, podemos hacerlo con el siguiente comando:

```bash
pip install django==x.y.z
```
siendo x.y.z la version que queremos instalar.

## Crear un proyecto en Django

Para cualquier duda sobre los comandos de Django, podemos utilizar el siguiente comando:

```bash
django-admin --help
```

Para crear un proyecto en Django se utiliza el siguiente comando:

```bash
django-admin startproject <nombre_del_proyecto>
```

El nombre del proyecto no debe tener espacios ni `-` si se quiere un nombre compuesto, se puede utilizar guion bajo `_`.

## Estructura de un proyecto en Django

- `manage.py`: es un script que ayuda con la administración del proyecto. Con él se pueden crear aplicaciones, crear un servidor de desarrollo, entre otras cosas.
- `nombre_del_proyecto/`: es la carpeta que contiene el proyecto.
  - `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
  - `settings.py`: es el archivo de configuración del proyecto. `-Importante`
  - `urls.py`: es el archivo que contiene las urls del proyecto. `-Importante`
  - `wsgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción.
  - `asgi.py`: es el archivo que contiene la configuración para desplegar el proyecto en producción con ASGI.

## Correr el servidor

Para correr el servidor de desarrollo de Django se utiliza el siguiente comando (debe estar en la carpeta del proyecto a la altura de `manage.py`):

```bash
python manage.py runserver
```
si tienes dudas sobre los comandos de `manage.py` puedes utilizar el siguiente comando:

```bash
python manage.py --help
```

## Entendiendo la arquitectura MVT

- Modelo: es la representación de los datos que maneja el proyecto.
- Vista: es la logica de datos que maneja el proyecto.
- Template: es la representación visual de los datos que maneja el proyecto.

## Crear una aplicación en Django
A la altura de `manage.py` se utiliza el siguiente comando para crear una aplicación en Django:

```bash
python manage.py startapp <nombre_de_la_aplicacion>
```

## Estructura de una aplicación en Django

- `migrations/`: es la carpeta que contiene las migraciones de la aplicación.
- `__init__.py`: es un archivo que indica que la carpeta es un paquete de Python.
- `admin.py`: es el archivo de configuración del administrador de Django.
- `apps.py`: es el archivo de configuración de la aplicación.
- `models.py`: es el archivo que contiene los modelos de la aplicación.
- `tests.py`: es el archivo que contiene las pruebas de la aplicación.
- `views.py`: es el archivo que contiene las vistas de la aplicación.

## trabajar con la aplicacion en Django

Para trabajar con la aplicación en Django, debemos agregarla en el archivo `settings.py` en la variable `INSTALLED_APPS`.

```python  
INSTALLED_APPS = [
    ...
    'nombre_de_la_aplicacion',
    ...
]
```

### Crear una vista en Django

Para crear una vista en Django, debemos modificar el archivo `views.py` de la aplicación.

```python
def nombre_de_la_vista(request):

    return render(request, 'ruta/nombre_de_la_vista.html')
```

### Crear una URL en Django

Para crear una URL en Django, debemos modificar el archivo `urls.py` de la aplicación.

```python
from django.urls import path
from nombre_de_la_aplicacion.views import nombre_de_la_vista

urlpatterns = [
    ...
    path('ruta/', nombre_de_la_vista,),
    ...
]
```

### Crear una template en Django

Para crear una template en Django, debemos crear una carpeta llamada `templates` en la raiz de la aplicación y dentro de ella crear una carpeta con el nombre de la aplicación y dentro de esa carpeta crear el archivo `nombre_de_la_vista.html`.


#### Codigo python en template

Para agregar codigo python en una template de Django, se utiliza la siguiente sintaxis:

```html
{% codigo_python %}
```
siempre se debe cerrar el bloque de codigo python con la siguiente sintaxis:

```html
{% endcodigo_python %}
```
Algunos ejemplos Basicos de codigo python en template:

```html
{% if condicion %}
    ...
{% endif %}

{% for item in lista %}
    ...
{% endfor %}

{% block nombre_del_bloque %}
    ...
{% endblock %}
```
