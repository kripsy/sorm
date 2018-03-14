from django.db import models

# Create your models here.


class TypeInformation(models.Model):
    name = models.CharField(max_length=90, verbose_name= "Тип информационного актива")
    id = models.AutoField(primary_key=True)

class CategoryInformation(models.Model):
    name = models.CharField(max_length=90, verbose_name= "Категория информационного актива")
    id = models.AutoField(primary_key=True)


class InformationAsset(models.Model):
    name = models.CharField(max_length=90, verbose_name="Наименование информационного актива")
    type_information = models.ForeignKey('TypeInformation', verbose_name="Тип информационного актива")
    category_information = models.ForeignKey('CategoryInformation', verbose_name="Категория информационного актива")
    id = models.AutoField(primary_key=True)