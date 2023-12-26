from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    age=models.IntegerField()
    fname=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
