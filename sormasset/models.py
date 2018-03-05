from django.db import models

# Create your models here.


class LevelOfInformationSecurity(models.Model):
    name = models.CharField(max_length=128)


#class TypeOfInformationAsset(models.Model):
