from .models import PlatinumModel,goldModel,silverModel
from django import forms
from django.contrib.auth.models import User

class  PlatinumForms(forms.ModelForm):
    class Meta:
        model = PlatinumModel
        fields = "__all__"
class  goldForms(forms.ModelForm):
    class Meta:
        model = goldModel
        fields = "__all__"
class  silverForms(forms.ModelForm):
    class Meta:
        model = silverModel
        fields = "__all__"

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]