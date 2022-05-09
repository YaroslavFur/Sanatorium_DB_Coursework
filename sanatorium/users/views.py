from multiprocessing import context
from tkinter import N
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from users.models import Patient, Employee

from .forms import SignUpForm, ProfileEditForm


def profile(request):
  context={'user': request.user}

  try:
    employee = Employee.objects.get(user_id=request.user.id)
  except Employee.DoesNotExist:
    employee = None
  if employee:
    context['employee'] = employee

  try:
    patient = Patient.objects.get(user_id=request.user.id)
  except Patient.DoesNotExist:
    patient = None
  if patient:
    context['patient']=patient

  return render(request, template_name='profile.html', context=context)
  

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
          return redirect('users:profile')
  else:
      form = SignUpForm()
  return render(request, 'signup.html', {'form': form})


def profile_edit(request):
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
      return redirect('users:profile')
  else:
    form = ProfileEditForm(initial={
      "first_name": request.user.first_name,
      "second_name": request.user.second_name,
      "email": request.user.email})
  return render(request, 'profileedit.html', {'form': form})