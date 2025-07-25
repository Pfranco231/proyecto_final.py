from django import forms
from .models import consolas

class consolasForm(forms.ModelForm):
    class Meta:
        model = consolas
        fields = ['imagen', 'modelo', 'empresa', 'precio', 'fecha_de_creacion']
        widgets = {
            'fecha_de_creacion': forms.SelectDateWidget(),
        }


class accesoriosForm(forms.Form):
    producto = forms.CharField(max_length=100)
    empresa = forms.CharField(max_length=100)
    duracion_bateria = forms.IntegerField()
    precio = forms.IntegerField()
    

class juegosForm(forms.Form):
    juego = forms.CharField(max_length=100)
    empresa = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=100)
    precio = forms.IntegerField()