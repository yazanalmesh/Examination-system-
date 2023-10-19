
from django.db import models

# Create your models here.

class Spec(models.Model):
    spec_name = models.CharField(unique=True)


class Category(models.Model):
    cat_number = models.IntegerField(unique=True)
    # specalize = models.ForeignKey(Spec, on_delete=models.CASCADE)

    
class Student(models.Model):
    username = models.CharField()
    specalize = models.ForeignKey(Spec, on_delete=models.CASCADE)
    group = models.ForeignKey(Category , on_delete=models.CASCADE)

class Teacher(models.Model):
    username = models.CharField(unique=True)
    password = models.CharField()



