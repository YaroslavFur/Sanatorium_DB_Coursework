from tkinter.tix import Tree
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import User

 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    second_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'email',)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.second_name = self.cleaned_data["second_name"]
        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    second_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'email', 'password')

    def save(self, commit=True):
        user = super(ProfileEditForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.second_name = self.cleaned_data["second_name"]
        user.set_password(self.clean_password())
        if commit:
            user.save()
        return user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password