from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.title} by {self.author}'


class School(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 20)
    year = models.DateField()

    def __str__(self):
        return f'{self.name} established on {self.year}'
    
class User(AbstractUser):
    surname = models.CharField(max_length = 50)
    firstname = models.CharField(max_length = 50)
    middlename = models.CharField(max_length = 50, blank = True)
    phone_number = models.CharField(max_length = 20, blank = True)
    address = models.CharField(max_length = 255)

    def __str__(self):
        return self.username
