from users.models import Employee, Patient

class MeAccessManager():
  @staticmethod
  def am_i_employee(self=None, request=None):
    try:
      if self:
        employee = Employee.objects.get(user_id=self.request.user.id)
      else:
        employee = Employee.objects.get(user_id=request.user.id)
    except Employee.DoesNotExist:
      return False
    return True
  
  @staticmethod
  def am_i_patient(self=None, request=None):
    try:
      if self:
        patient = Patient.objects.get(user_id=self.request.user.id)
      else:
        patient = Patient.objects.get(user_id=request.user.id)
    except Patient.DoesNotExist:
      return False
    return True

  @staticmethod
  def am_i_manager(self=None, request=None):
    try:
      if self:
        employee = Employee.objects.get(user_id=self.request.user.id)
      else:
        employee = Employee.objects.get(user_id=request.user.id)
    except Employee.DoesNotExist:
      return False
    if not employee.speciality == 'manager':
      return False
    return True