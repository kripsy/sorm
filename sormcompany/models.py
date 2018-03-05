from django.db import models

# Create your models here.

class TypeCompany(models.Model):
    name = models.CharField(max_length=90, unique= True, verbose_name= "Тип организационной единицы")
    id = models.AutoField(primary_key=True)

class Company(models.Model):
    name = models.CharField(max_length=90, unique= True, verbose_name= "Наименование организационной единицы")
    type_company = models.OneToOneField('TypeCompany', verbose_name= "Тип организационной единицы")
    parent_company = models.ForeignKey('Company', null= True, verbose_name= "Родительская организация")
    id = models.AutoField(primary_key=True)