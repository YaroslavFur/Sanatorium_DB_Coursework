from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from payments.models import Bill
from meclasses.MeSignalManager import *

from therapy.models import Disease, Symptom
from cooperation.models import Hospital

patient_default_change = 30
employee_default_change = 50


class UserManager(BaseUserManager):

  def _create_user(self, first_name, second_name, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        first_name=first_name,
        second_name=second_name,
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, first_name, second_name, email, password, **extra_fields):
    return self._create_user(first_name, second_name, email, password, False, False, **extra_fields)

  def create_superuser(self, first_name, second_name, email, password, **extra_fields):
    user=self._create_user(first_name, second_name, email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
  first_name = models.CharField(max_length=254)
  second_name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254, unique=True)
  hospitals = models.ManyToManyField(Hospital, blank=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  last_login = models.DateTimeField(null=True, blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'second_name']

  objects = UserManager()

  def __str__(self):
    return f"{self.first_name} {self.second_name}"

  def get_absolute_url(self):
      return "/users/%i/" % (self.pk)


class Employee(models.Model):
  user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
  speciality = models.CharField(max_length=20)
  bill = models.OneToOneField(Bill, on_delete=models.PROTECT, blank=True)

  def __str__(self):
    return f"{self.speciality} {self.user.first_name} {self.user.second_name}"

  def save(self, *args, **kwargs):
    if not hasattr(self, 'bill'):
      bill = Bill()
      bill.info = f"employee {self}"
      bill.change = employee_default_change
      bill.save()
      self.bill = bill
    super(Employee, self).save(*args, **kwargs)

delete_employee_signal(Employee)


class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
  diseases = models.ManyToManyField(Disease, blank=True)
  symptoms = models.ManyToManyField(Symptom, blank=True)
  hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT, null=True, blank=True)
  bill = models.OneToOneField(Bill, on_delete=models.PROTECT, null=True, blank=True)

  def save(self, *args, **kwargs):
    if self.hospital == None:
      bill = Bill()
      bill.info = f"patient {self}"
      bill.change = patient_default_change
      bill.save()
      self.bill = bill
    super(Patient, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.user.first_name} {self.user.second_name}"

delete_patient_signal(Patient)