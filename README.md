# Control REST

## Descripcion

Esta aplicacion para django es una end-point para que la aplicacion de f2 se connecte y utilize la base de datos del modulo de asistencia.

## instalacion

1. Clonar repositorio al root del proyecto con:

```bash
git clone https://github.com/Grupo42018/asistenciaREST.git
```

2. Instalar requerimientos:

```bash
pip install django-rest-framework django-filter
```

3. Agregar las siguientes aplicaciones a INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'REST',
]
```

4. Copiar lo siguiente en settings.py:

```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}
```

5. Agregar lo siguiente en urls.py:

```python
...
from REST import urls as resturl
urlpatterns = [
    ...,
    url(r'^api/', include(resturl.urlpatterns)),
]
```

## Utilizacion

Al terminar la instalacion se agregara la url `api/` que poseera:

    * `students/`: esta url tiene la posibilidad de filtrar los alumnos mediante formularios en get, si no se proporciona ningun filtro se devolveran todos los alumnos. 
    * `parents/`: esta url tiene la posibilidad de filtrar los tutores mediante formularios en get, si no se proporciona ningun filtro se devolveran todos los tutores. 

    * `preceptors/`: esta url tiene la posibilidad de filtrar los preceptores mediante formularios en get, si no se proporciona ningun filtro se devolveran todos los preceptores. 

    * `years/`: esta url tiene la posibilidad de filtrar los Years mediante formularios en get, si no se proporciona ningun filtro se devolveran todos los Years. 

    * `registros/`: esta url tiene la posibilidad de filtrar los registros de faltas mediante formularios en get, si no se proporciona ningun filtro se devolveran todos los registros de faltas. 
    
    * `absence/`: esta url posee la prosibilidad de brindar un id para recuperar 1 solo registro mediante GET o crear, actualizar una ausencia mediante los metodos PUT y POST.
