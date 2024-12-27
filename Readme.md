# Punto Científico

**Punto Científico** es una plataforma web desarrollada con Django que ofrece productos y equipos de laboratorio y científicos. El sitio está diseñado para facilitar la compra y venta de materiales de alta calidad para profesionales del área científica.


## Características

* **Catálogo de productos** : Navega por una amplia gama de productos categorizados según su uso y aplicación.
* **Sistema de usuarios** : Registro e inicio de sesión para clientes.
* **Panel de administración** : Gestión de productos y usuarios mediante el panel de administración de Django.

## Tecnologías utilizadas

* **Lenguaje de programación** : Python
* **Framework web** : Django
* **Base de datos** : SQLite (por defecto)
* **Frontend** : HTML, CSS y Bootstrap
* **Control de versiones** : Git

## Instalación y configuración

### Requisitos previos

Asegúrate de tener instalados:

* Python 3.8+
* pip
* Git

### Pasos de instalación

1- Clonar el repositorio

```
git clone https://github.com/tu-usuario/punto-cientifico.git
cd punto-cientifico
```

2- Crear un entorno virtual y activarlo

```
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3- Instalar las dependencias

```
pip install -r requirements.txt
```

4- Comprobar las migraciones

```
python manage.py makemigrations
```

5- Aplicar las migraciones de la base de datos

```
python manage.py migrate
```

6- Iniciar el servidor de desarrollo

```
python manage.py runserver
```

Accede al sitio en [http://localhost:8000]().

link del video explicando la pagina: https://youtu.be/HsyH9r4ed4U?si=W7vGsFzNZirKYwzS
