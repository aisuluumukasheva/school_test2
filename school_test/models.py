from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
