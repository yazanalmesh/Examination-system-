from django import forms
from .models import Student, Teacher
class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = Teacher
        fields = ("username", "password")
