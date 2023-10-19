from django import forms
from .models import Students, Teachers
class AddStudent(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

class TeacherLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = Teachers
        fields = ("username", "password")
