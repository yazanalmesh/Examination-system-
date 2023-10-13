# exam/forms.py
from django import forms
from .models import Exam, Category


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
