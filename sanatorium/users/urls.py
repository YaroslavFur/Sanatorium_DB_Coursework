from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import profile, signup, profile_edit

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/main'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login'), name='logout'),
    path('profile/',  login_required(profile), name='profile'),
    path('profile/edit', login_required(profile_edit), name='profile_edit'),
    path('signup/', signup, name='signup')
]