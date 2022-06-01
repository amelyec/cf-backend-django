# Commands for django project

## Check Python Version
py --version
Python 3.10.4

## Create Virtual Environment
py -m venv .venv

## Activate Virtual Environment

.venv\Scripts\activate

## Install django and djangorestframework
pip install django
pip install djangorestframework

## Create project
django-admin startproject core .

## Create migrations
py manage.py migrate

## SuperUser
py manage.py createsuperuser

[Admin Link](http://127.0.0.1:8000/admin/auth/user/)

## Create application
django-admin startapp app

## Add app to installed apps
INSTALLED_APPS = [
    'app',
    ....
]

## Create Model and run migration
py manage.py makemigrations app
py manage.py migrate app

## Git Push

echo "# cf-backend-django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:amelyec/cf-backend-django.git
git push -u origin main
