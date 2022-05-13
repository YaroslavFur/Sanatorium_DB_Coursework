import imp
from tkinter.messagebox import NO
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from multiprocessing import context, get_context
from django.shortcuts import render, redirect
from .models import Hospital
from payments.models import Bill
from meclasses.MeAccessManager import MeAccessManager


class HospitalList(ListView):
  model = Hospital
  context_object_name = "hospital_list"
  template_name = 'hospital_crud/hospital_list.html'


class HospitalUpdate(UserPassesTestMixin, UpdateView):
  model = Hospital
  fields = ['name']
  context_object_name = 'hospital'
  template_name = 'hospital_crud/hospital_update.html'
  
  def get_success_url(self):
    return reverse('cooperation:hospital_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class HospitalCreate(UserPassesTestMixin, CreateView):
  model = Hospital
  fields = ['name']
  template_name = 'hospital_crud/hospital_create.html'

  def get_success_url(self):
    return reverse('cooperation:hospital_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class HospitalDelete(UserPassesTestMixin, DeleteView):
  model = Hospital
  context_object_name = 'hospital'
  template_name = 'hospital_crud/hospital_delete.html'

  def get_success_url(self):
    return reverse('cooperation:hospital_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)