from django.db import models

# Create your models here.

class Student_Data(models.Model):
    name = models.CharField(max_length=250)
    roll_no = models.IntegerField()




