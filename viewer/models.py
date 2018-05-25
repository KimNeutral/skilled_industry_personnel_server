from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=50)
    email = models.CharField(max_length=200)


class Recruit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

