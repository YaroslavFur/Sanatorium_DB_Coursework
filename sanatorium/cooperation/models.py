from re import I
from tkinter.tix import Tree
from django.db import models
from payments.models import Bill
from meclasses.MeSignalManager import *

hospital_default_change = 20


class Hospital(models.Model):
  name = models.CharField(max_length=254)
  bill = models.OneToOneField(Bill, on_delete=models.PROTECT, blank=True)
  
  def __str__(self):
    return f"{self.name}"

  def save(self, *args, **kwargs):
    if not hasattr(self, 'bill'):
      bill = Bill()
      bill.info = f"hospital {self}"
      bill.change = hospital_default_change
      bill.save()
      self.bill = bill
    super(Hospital, self).save(*args, **kwargs)

delete_hospital_signal(Hospital)