from django.db import models

class Disease(models.Model):
  name = models.CharField(max_length=254)
  description_ref = models.CharField(max_length=500, null=True, blank=True)
  
  def __str__(self):
    return f"{self.name}"


class Symptom(models.Model):
  name = models.CharField(max_length=254)
  description_ref = models.CharField(max_length=500, null=True, blank=True)
  
  def __str__(self):
    return f"{self.name}"
