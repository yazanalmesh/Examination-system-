
from django.db import models

# Create your models here.


class Students(models.Model):
    username = models.CharField()
    specalize = models.ForeignKey(spec_name, on_delete=models.CASCADE)
    group = models.ForeignKey(cat_number , on_delete=models.CASCADE)

class Teachers(models.Model):
    username = models.CharField(unique=True)
    password = models.CharField()

class Categories(models.Model):
    cat_number = models.IntegerField(unique=True)
    specalize = models.ForeignKey(spec_name, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_number

class Specalizes(models.Model):
    spec_name = models.CharField(unique=True)

    def __str__(self):
        return self.spec_name