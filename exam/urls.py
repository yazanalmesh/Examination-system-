# exam/urls.py
from django.urls import path
from . import views
app_name = 'exam'
urlpatterns = [
    path('exams/', views.exam_list, name='exam_list'),
    path('categories/', views.category_list, name='category_list'),
]
