import imp
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from multiprocessing import context, get_context
from django.shortcuts import render, redirect
from .models import Disease, Symptom
from meclasses.MeAccessManager import MeAccessManager

class DiseaseList(ListView):
  model = Disease
  context_object_name = "disease_list"
  template_name = 'disease_crud/disease_list.html'


class DiseaseUpdate(UserPassesTestMixin, UpdateView):
  model = Disease
  fields = ['name', 'description_ref']
  context_object_name = 'disease'
  template_name = 'disease_crud/disease_update.html'
  
  def get_success_url(self):
    return reverse('therapy:disease_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class DiseaseCreate(UserPassesTestMixin, CreateView):
  model = Disease
  fields = ['name', 'description_ref']
  template_name = 'disease_crud/disease_create.html'

  def get_success_url(self):
    return reverse('therapy:disease_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class DiseaseDelete(UserPassesTestMixin, DeleteView):
  model = Disease
  context_object_name = 'disease'
  template_name = 'disease_crud/disease_delete.html'

  def get_success_url(self):
    return reverse('therapy:disease_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)



class SymptomList(ListView):
  model = Symptom
  context_object_name = "symptom_list"
  template_name = 'symptom_crud/symptom_list.html'


class SymptomUpdate(UserPassesTestMixin, UpdateView):
  model = Symptom
  fields = ['name', 'description_ref']
  context_object_name = 'symptom'
  template_name = 'symptom_crud/symptom_update.html'
  
  def get_success_url(self):
    return reverse('therapy:symptom_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class SymptomCreate(UserPassesTestMixin, CreateView):
  model = Symptom
  fields = ['name', 'description_ref']
  template_name = 'symptom_crud/symptom_create.html'

  def get_success_url(self):
    return reverse('therapy:symptom_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class SymptomDelete(UserPassesTestMixin, DeleteView):
  model = Symptom
  context_object_name = 'symptom'
  template_name = 'symptom_crud/symptom_delete.html'

  def get_success_url(self):
    return reverse('therapy:symptom_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)