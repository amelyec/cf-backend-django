from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frameworks/', views.framework_list, name='frameworks')
]
