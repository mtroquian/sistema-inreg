from django.utils import timezone

from django.db import models

# Create your models here.
class NumeroInforme(models.Model):
    id = models.AutoField(primary_key=True)

    numero_informe = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un nuevo registro
            year = timezone.now().year % 100
            registros_del_año = NumeroInforme.objects.filter(numero_informe__contains=f'{year}').count()
            reg = NumeroInforme.objects.filter(numero_informe__contains=f'{year}').count()
            nuevo_numero = f"{registros_del_año + 1}-{year:02d}"
            print (reg)
            print (year)
            self.numero_informe = nuevo_numero
        super().save(*args, **kwargs)

    tanque = models.CharField(max_length=100)
    inspeccion_efectuada = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    tomado_por = models.CharField(max_length=100)


class NumeroIncr(models.Model):
    id = models.AutoField(primary_key=True)
    numero_informe = models.CharField(max_length=100)
    tanque = models.CharField(max_length=100)
    inspeccion_efectuada = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    tomado_por = models.CharField(max_length=100)


class CantidadGenerar(models.Model):
    id = models.AutoField(primary_key=True)
    numero_informe = models.CharField(max_length=100)


