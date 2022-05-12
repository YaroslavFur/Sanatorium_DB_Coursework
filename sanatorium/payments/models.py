from datetime import datetime
from math import floor
from tkinter import N
from django.db import models

class Bill(models.Model):
  info = models.CharField(max_length=254)
  amount = models.FloatField(default=0)
  last_change = models.DateTimeField()
  change = models.IntegerField(default=0)
  
  def __str__(self):
    return f"{self.info}"


def getter(instance, **kwargs):
  now = datetime.now()
  delta_seconds = (now - instance.last_change).total_seconds()
  if hasattr(instance, 'hospital'):
    current_change = len(instance.hospital.patient_set.all()) * instance.change
  else:
    current_change = instance.change
  instance.amount += delta_seconds / 60.0 / 60.0 * current_change
  instance.last_change = now
  instance.save()
  instance.current_change = current_change

models.signals.post_init.connect(getter, Bill)