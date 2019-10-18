from django.db import models

# Create your models here.

from django.db import models
class Employee(models.Model):
 first_name = models.CharField(max_length=20)
 last_name = models.CharField(max_length=20)
 designation = models.CharField(max_length=50)
 def __str__(self):
  return self.first_name + " " + self.last_name
