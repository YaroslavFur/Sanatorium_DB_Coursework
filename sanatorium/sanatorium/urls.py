"""sanatorium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import main

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls', namespace='accounts'), name='accounts'),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('therapy/', include('therapy.urls', namespace='therapy'), name='therapy'),
    path('cooperation/', include('cooperation.urls', namespace='cooperation'), name='cooperation'),
    path('payments/', include('payments.urls', namespace='payments'), name='payments'),

    path('', login_required(main), name=''),
    path('main/', login_required(main), name='main')
]
