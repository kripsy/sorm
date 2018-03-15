from django.db import models
# Create your models here.






class Assessment(models.Model):
    name = models.CharField(max_length=90, verbose_name="Наименование Оценки")
#    assessment_company = models.ForeignKey('Company', verbose_name="Организация, которая попадает под оценку")
#    assessment_type_information = models.ForeignKey('CategoryInformation', verbose_name="Категория информационного актива")
#    information_controls = models.ManyToManyField(Control)
#    information_class_controls = models.ManyToManyField(ClassControl, verbose_name="Класс СЗИ")
#    id = models.AutoField(primary_key=True)
