from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64, null=True)
    dob = models.DateField()
