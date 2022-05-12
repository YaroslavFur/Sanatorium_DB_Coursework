from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import BillList, BillUpdate, pay_bill, pay_hospital_bill, get_wages

app_name = 'payments'

urlpatterns = [
  path('bill_list/', login_required(BillList.as_view()), name='bill_list'),
  path('bill/<int:pk>/', login_required(BillUpdate.as_view()), name='bill_update'),

  path('pay_bill/<int:pk>/', login_required(pay_bill), name='pay_bill'),
  path('pay_hospital_bill/<int:pk>/', login_required(pay_hospital_bill), name='pay_hospital_bill'),
  path('get_wages/<int:pk>/', login_required(get_wages), name='get_wages'),
]