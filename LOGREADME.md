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

## 