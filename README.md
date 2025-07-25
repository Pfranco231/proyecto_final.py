# Proyecto Final - Aplicación Django

Este repositorio contiene el código fuente y la documentación del proyecto final desarrollado por Franco, basado en Django.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Contacto](#contacto)

## Descripción

Proyecto desarrollado en Django que simula una web de coleccionistas de consolas. Permite a los usuarios registrarse, iniciar sesión, gestionar su perfil con avatar e interactuar con una base de datos de consolas mediante funcionalidades CRUD (crear, leer, actualizar y eliminar).

### VIDEO: Del funcionamiento de la pagina:
'''bash
INSERT VIDEO MEDIA
'''

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/proyecto-final.git
    cd proyecto-final
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

5. (Opcional) Crea un superusuario para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

## Uso

Ejecuta el servidor de desarrollo de Django:
```bash
python manage.py runserver
```

Accede a la aplicación en [http://localhost:8000](http://localhost:8000) y explora las funcionalidades principales.

## Estructura del Proyecto

```
entregable_3 (si este proyecto tomo como base la entrega 3)/
├── entregable_3/       # Código fuente principal
├── main/               # aplicacion principal
├── media/              # donde los usuarios suben sus imagenes
├── static/             # imagenes estaticas
├── templates/          # Es donde se aloja el html padre
├── usuarios/           # La app de registro y logeo de los usuarios
├── manage.py           # Script de gestión de Django
├── requirements.txt    # Dependencias del proyecto
├── ../README.md           # Este archivo
├── [otros archivos importantes]
```

## Dependencias

- Django
- Pillow
- sqlparse
- asgiref

> Estas se instalan automáticamente con `pip install -r requirements.txt`.

## Contribución

Las contribuciones son bienvenidas. Podés abrir un *issue* o enviar un *pull request* para sugerencias o mejoras.

## Contacto

📧 papeschifranco@gmail.com