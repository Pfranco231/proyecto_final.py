from django import forms

class consolasForm(forms.Form):
    modelo = forms.CharField(max_length=100)
    empresa = forms.CharField(max_length=100)
    precio = forms.IntegerField()
    fecha_de_creacion = forms.DateField(label='Fecha de Inicio', widget=forms.SelectDateWidget())


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