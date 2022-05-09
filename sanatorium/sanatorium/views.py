
from django.shortcuts import render, redirect


def main(request):
  context = {'user': request.user}
  return render(request, template_name='main.html', context=context)