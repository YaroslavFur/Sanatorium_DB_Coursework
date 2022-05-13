from datetime import datetime
import imp
from tkinter.messagebox import NO
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from multiprocessing import context, get_context
from django.shortcuts import render, redirect
from payments.models import Bill, Payment
from meclasses.MeAccessManager import MeAccessManager

def create_payment(bill, info):
  payment = Payment()
  payment.bill = bill
  payment.info = info
  payment.amount = bill.amount
  payment.conducted = datetime.now()
  bill.amount = 0
  payment.save()  
  bill.save()

def pay_bill(request, pk):
  bill = Bill.objects.get(id=pk)
  if hasattr(bill, 'patient'):
    if bill.patient.user_id == request.user.id:
      create_payment(bill, bill.info + " pays bill")
      return redirect(reverse('users:myprofile'))
  return HttpResponseForbidden('<h1>403 Forbidden</h1>')

  
def pay_hospital_bill(request, pk):
  bill = Bill.objects.get(id=pk)
  if hasattr(bill, 'hospital'):
    for loopuser in bill.hospital.user_set.all():
      if loopuser.id == request.user.id:
        create_payment(bill, str(loopuser) + " pays hospital bill " + bill.info)
        return redirect(reverse('users:myprofile'))
  return HttpResponseForbidden('<h1>403 Forbidden</h1>')

  
def get_wages(request, pk):
  bill = Bill.objects.get(id=pk)
  if hasattr(bill, 'employee'):
    if bill.employee.user_id == request.user.id:
      create_payment(bill, bill.info + " gets wages")
      return redirect(reverse('users:myprofile'))
  return HttpResponseForbidden('<h1>403 Forbidden</h1>')


class BillList(ListView):
  model = Bill
  context_object_name = "bill_list"
  template_name = 'bill_crud/bill_list.html'

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class BillUpdate(UserPassesTestMixin, UpdateView):
  model = Bill
  fields = ['change']
  context_object_name = 'bill'
  template_name = 'bill_crud/bill_update.html'
  
  def get_success_url(self):
    return reverse('payments:bill_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)

class PaymentList(ListView):
  model = Payment
  context_object_name = "payment_list"
  template_name = 'payment_crud/payment_list.html'

  def test_func(self):
    return MeAccessManager.am_i_manager(self)