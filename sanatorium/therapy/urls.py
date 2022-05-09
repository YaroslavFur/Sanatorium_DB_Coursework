from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import diseases, symptoms

app_name = 'therapy'

urlpatterns = [
  path('diseases/', login_required(diseases), name='diseases'),
  path('symtoms/', login_required(symptoms), name='symptoms')
]