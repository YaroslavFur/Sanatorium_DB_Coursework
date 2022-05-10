from multiprocessing import context
from tkinter import N
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from meclasses.MeAccessManager import MeAccessManager
from users.models import Patient, Employee, User
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import SignUpForm, ProfileEditForm


def myprofile(request):
  context = {'user': request.user}

  return render(request, template_name='myprofile.html', context=context)
  

def signup(request):
  if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
          user = form.save()
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(request, email=user.email, password=raw_password)
          if user is not None:
              login(request, user)
          else:
              print("user is not authenticated")
          return redirect('users:myprofile')
  else:
      form = SignUpForm()
  return render(request, 'signup.html', {'form': form})


def myprofile_edit(request):
  if request.method == 'POST':
    form = ProfileEditForm(request.POST, instance=request.user)
    form.actual_user = request.user
    if form.is_valid():
      user = form.save()
      user = authenticate(request, email=user.email, password=form.cleaned_data["password"])
      if user is not None:
        login(request, user)
      else:
        print("user is not authenticated")
      return redirect('users:myprofile')
  else:
    form = ProfileEditForm(initial={
      "first_name": request.user.first_name,
      "second_name": request.user.second_name,
      "email": request.user.email})
  return render(request, 'myprofileedit.html', {'form': form})


def profile(request, pk):
  if pk == request.user.id:
    return redirect(reverse('users:myprofile'))
  context = {'user': request.user}
  try:
    user = User.objects.get(id=pk)
    context['profile'] = user
    return render(request, template_name='profile.html', context=context)
  except User.DoesNotExist:
    return HttpResponseNotFound('<h1>404 Page not found</h1>')



class EmployeeList(UserPassesTestMixin, ListView):
  model = Employee
  context_object_name = "employee_list"
  template_name = 'employee_crud/employee_list.html'
  
  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class EmployeeUpdate(UserPassesTestMixin, UpdateView):
  model = Employee
  fields = ['speciality']
  context_object_name = 'employee'
  template_name = 'employee_crud/employee_update.html'
  
  def get_success_url(self):
    return reverse('users:employee_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class EmployeeCreate(UserPassesTestMixin, CreateView):
  model = Employee
  fields = ['user', 'speciality']
  template_name = 'employee_crud/employee_create.html'

  def get_success_url(self):
    return reverse('users:employee_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class EmployeeDelete(UserPassesTestMixin, DeleteView):
  model = Employee
  context_object_name = 'employee'
  template_name = 'employee_crud/employee_delete.html'

  def get_success_url(self):
    return reverse('users:employee_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)



class PatientList(UserPassesTestMixin, ListView):
  model = Patient
  context_object_name = "patient_list"
  template_name = 'patient_crud/patient_list.html'
  
  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class PatientUpdate(UserPassesTestMixin, UpdateView):
  model = Patient
  fields = ['diseases', 'symptoms']
  context_object_name = 'patient'
  template_name = 'patient_crud/patient_update.html'
  
  def get_success_url(self):
    return reverse('users:patient_list')

  def test_func(self):
    return MeAccessManager.am_i_employee(self)


class PatientCreate(UserPassesTestMixin, CreateView):
  model = Patient
  fields = ['user']
  template_name = 'patient_crud/patient_create.html'

  def get_success_url(self):
    return reverse('users:patient_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)


class PatientDelete(UserPassesTestMixin, DeleteView):
  model = Patient
  context_object_name = 'patient'
  template_name = 'patient_crud/patient_delete.html'

  def get_success_url(self):
    return reverse('users:patient_list')

  def test_func(self):
    return MeAccessManager.am_i_manager(self)



class UserList(ListView):
  model = User
  context_object_name = "user_list"
  template_name = 'user_crud/user_list.html'