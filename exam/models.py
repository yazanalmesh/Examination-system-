from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exam(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='exam_covers/')
    keyword = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
