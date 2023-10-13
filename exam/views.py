# exam/views.py
from django.shortcuts import render
from .models import Exam, Category
from .forms import ExamForm, CategoryForm


def exam_list(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'exam/exam_list.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'exam/category_list.html', context)
