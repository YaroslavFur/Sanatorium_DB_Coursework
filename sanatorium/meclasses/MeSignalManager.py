from django.dispatch import receiver
from django.db.models.signals import post_delete

def delete_employee_signal(Employee):
  @receiver(post_delete, sender=Employee)
  def delete_bill(sender, instance, **kwargs):
    if instance.bill:
      instance.bill.delete()

def delete_patient_signal(Patient):
  @receiver(post_delete, sender=Patient)
  def delete_bill(sender, instance, **kwargs):
    if instance.bill:
      instance.bill.delete()

def delete_hospital_signal(Hospital):
  @receiver(post_delete, sender=Hospital)
  def delete_bill(sender, instance, **kwargs):
    if instance.bill:
      instance.bill.delete()