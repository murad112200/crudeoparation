from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)


    def __str__(salf):
        return salf.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    emil = models.EmailField()
    dep = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=20)


    def __str__(salf):
        return salf.name
    

class Store(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file = models.FileField()


    def __str__(self):
        return self.name
