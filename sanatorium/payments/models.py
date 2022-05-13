from datetime import datetime
from django.db import models

autodelete_payment_log_after_years = 2

class Bill(models.Model):
  info = models.CharField(max_length=254, null=True)
  amount = models.FloatField(default=0, null=True)
  last_change = models.DateTimeField(auto_now_add=True, null=True)
  change = models.IntegerField(default=0, null=True)
  
  def __str__(self):
    return f"{self.info}"


def bill_get(instance, **kwargs):
  now = datetime.now()
  if instance.last_change:
    delta_seconds = (now - instance.last_change).total_seconds()
  else:
    delta_seconds = 0
  if hasattr(instance, 'hospital'):
    current_change = len(instance.hospital.patient_set.all()) * instance.change
  else:
    current_change = instance.change
  instance.amount += delta_seconds / 60.0 / 60.0 * current_change
  instance.last_change = now
  instance.save()
  instance.current_change = current_change

models.signals.post_init.connect(bill_get, Bill)


class Payment(models.Model):
  bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
  info = models.CharField(max_length=254)
  amount = models.FloatField()
  conducted = models.DateTimeField()

  def save(self, *args, **kwargs):
    last_payment = Payment.objects.order_by('conducted')[0]
    if datetime.now().year - last_payment.conducted.year > autodelete_payment_log_after_years:
      last_payment.delete()
    super(Payment, self).save(*args, **kwargs)

  class Meta:
        ordering = ['-conducted']

  def __str__(self):
    return f"{self.info}"