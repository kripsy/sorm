from django.db import models

# Create your models here.

class TypeCompany(models.Model):
    name = models.CharField(max_length=90, verbose_name= "Тип организационной единицы")
    id = models.AutoField(primary_key=True)

class Company(models.Model):
    name = models.CharField(max_length=90, verbose_name= "Наименование организационной единицы")
    type_company = models.ForeignKey('TypeCompany', verbose_name= "Тип организационной единицы")
    id = models.AutoField(primary_key=True)