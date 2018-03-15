from django.db import models
from sorminformation.models import *
# Create your models here.

class TypeRealization(models.Model):
    name = models.CharField(max_length=90, verbose_name="Тип реализации")
    id = models.AutoField(primary_key=True)

class ClassControl(models.Model):
    name = models.CharField(max_length=90, verbose_name="Класс СЗИ")
    id = models.AutoField(primary_key=True)

class Control(models.Model):
    name = models.CharField(max_length=90, verbose_name="Наименование контрмеры")
    type_realization = models.ForeignKey(TypeRealization, verbose_name='Тип реализации')
    id = models.AutoField(primary_key=True)