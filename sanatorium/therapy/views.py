from multiprocessing import context
from django.shortcuts import render
from .models import Disease, Symptom

def diseases(request):
  context={'diseases': Disease.objects.all}
  return render(request=request, template_name='diseases.html', context=context)


def symptoms(request):
  pass