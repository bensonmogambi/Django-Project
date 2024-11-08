from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=22)
    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=22)
    age = models.IntegerField()

    def __str__(self):
        return self.name




