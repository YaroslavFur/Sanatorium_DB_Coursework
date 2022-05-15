from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import HospitalList, HospitalCreate, HospitalUpdate, HospitalDelete

app_name = 'cooperation'

urlpatterns = [
  path('hospital_list/', login_required(HospitalList.as_view()), name='hospital_list'),
  path('hospital_create/', login_required(HospitalCreate.as_view()), name='hospital_create'),
  path('hospital/<int:pk>/', login_required(HospitalUpdate.as_view()), name='hospital_update'),
  path('hospital_delete/<int:pk>/', login_required(HospitalDelete.as_view()), name='hospital_delete'),

  
]