from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import myprofile, signup, myprofile_edit, profile, \
                    EmployeeList, EmployeeCreate, EmployeeUpdate, EmployeeDelete, \
                    PatientList, PatientCreate, PatientUpdate, PatientDelete, \
                    UserList

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/main'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login'), name='logout'),
    path('myprofile/',  login_required(myprofile), name='myprofile'),
    path('profile/<int:pk>',  login_required(profile), name='profile'),
    path('myprofile_edit', login_required(myprofile_edit), name='myprofile_edit'),
    path('signup/', signup, name='signup'),

    path('employee_list/', login_required(EmployeeList.as_view()), name='employee_list'),
    path('employee_create/', login_required(EmployeeCreate.as_view()), name='employee_create'),
    path('employee/<int:pk>/', login_required(EmployeeUpdate.as_view()), name='employee_update'),
    path('employee_delete/<int:pk>/', login_required(EmployeeDelete.as_view()), name='employee_delete'),
    
    path('patient_list/', login_required(PatientList.as_view()), name='patient_list'),
    path('patient_create/', login_required(PatientCreate.as_view()), name='patient_create'),
    path('patient/<int:pk>/', login_required(PatientUpdate.as_view()), name='patient_update'),
    path('patient_delete/<int:pk>/', login_required(PatientDelete.as_view()), name='patient_delete'),

    path('user_list/', login_required(UserList.as_view()), name='user_list')
]