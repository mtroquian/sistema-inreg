from django import forms
from .models import NumeroInforme, NumeroIncr
from django.utils import timezone

class NumeroInformeForm(forms.ModelForm):
    class Meta:
        model = NumeroInforme
        fields = '__all__'

class GenerarNumeroForm(forms.ModelForm):

    
    class Meta:
        model = NumeroIncr
        fields = ['tanque', 'inspeccion_efectuada', 'tipo', 'fecha', 'tomado_por']


    def generar_numero(self):
        year = timezone.now().year % 100
        registros_del_año = NumeroIncr.objects.filter(numero_informe__contains=f'{year}').count()
        nuevo_numero = f"{registros_del_año + 1}-{year:02d}"
        return nuevo_numero
    
    