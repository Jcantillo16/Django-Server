from django.db import models


# Create your models here.
class Persona(models.Model):
    tipo_documento = models.CharField(max_length=5)
    documento = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=500)

    class Meta():
        db_table='enersinc_persona'
