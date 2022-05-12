from re import I
from tkinter.tix import Tree
from django.db import models
from payments.models import Bill

class Hospital(models.Model):
  name = models.CharField(max_length=254)
  bill = models.OneToOneField(Bill, on_delete=models.PROTECT)
  
  def __str__(self):
    return f"{self.name}"