from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import DiseaseDelete, DiseaseList, DiseaseUpdate, DiseaseCreate, \
                    SymptomDelete, SymptomList, SymptomUpdate, SymptomCreate

app_name = 'therapy'

urlpatterns = [
  path('disease_list/', login_required(DiseaseList.as_view()), name='disease_list'),
  path('disease_create/', login_required(DiseaseCreate.as_view()), name='disease_create'),
  path('disease/<int:pk>/', login_required(DiseaseUpdate.as_view()), name='disease_update'),
  path('disease_delete/<int:pk>/', login_required(DiseaseDelete.as_view()), name='disease_delete'),

  path('symtom_list/', login_required(SymptomList.as_view()), name='symptom_list'),
  path('symtom_create/', login_required(SymptomCreate.as_view()), name='symptom_create'),
  path('symtom/<int:pk>/', login_required(SymptomUpdate.as_view()), name='symptom_update'),
  path('symtom_delete/<int:pk>/', login_required(SymptomDelete.as_view()), name='symptom_delete')
]