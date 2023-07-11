# Simple app - Terra Classic + Django
## Introduction
This tutorial enables you to initiate a Django application utilizing the Terra Classic blockchain and exhibit the most recent block
## Tutorial
### Virtual Environment
Create virtual environment <b>terra_classic_env</b>
```
python -m venv terra_classic_env
```

Activate the virtual environment on Window
```windows
terra_classic_env/Script/activate
```
or Linux
```linux
source terra_classic_env/bin/activate
```
### Installation
Installing <b>Django</b>
```
pip install django
```
Installing <b>Terra Classic SDK</b>
```
pip install terra-classic-sdk
```
### Creation of a new project
Use the standard django-admin script to create a project named <b>django_app</b>.
```
django-admin startproject django_app
```
### Creation of a new app
Create app <b>terra_app</b>
```
python manage.py startapp terra_app
```
Update <b>views.py</b> for connect terra classic blockchain and display the last block

<i>terra_app/views.py</i>
```python3
from django.http import HttpResponse
from terra_classic_sdk.client.lcd import LCDClient

# Create an instance of LCDClient to connect to the Terra Classic network
TERRA = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")


def index(request):
    # This view returns an HTTP response
    # It displays information about the last block on the Terra Classic blockchain

    # Use the TERRA object to retrieve the latest block information
    block_height = TERRA.tendermint.block_info()['block']['header']['height']

    # Format the block height information into a string
    response_content = "Terra app, last block {} on Terra Classic blockchain.".format(block_height)

    # Return the formatted string as an HTTP response
    return HttpResponse(response_content)
```
Add url on <b>django_app/urls.py</b>

<i>django_app/urls.py</i>
```python3
from django.contrib import admin
from django.urls import path
from terra_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]
```
### Configuration de settings.py
Add terra_app to <b>django_app/settings.py</b>

<i>django_app/settings.py</i>
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'terra_app',
]
```
### Run serveur
```
python manage.py runserver
```

You can see the result on http://127.0.0.1:8000/

![first_app](../img/simple_app_django.PNG)