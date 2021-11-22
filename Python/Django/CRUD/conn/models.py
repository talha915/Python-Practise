from django.db import connections
from django.db import models

# Create your models here.
class Employees(models.Model):
    id = models.IntegerField(),
    emp_name = models.CharField(max_length=250),
    age = models.IntegerField()

    class Meta:
        db_table = "test_django_emp"