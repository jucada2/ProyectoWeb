from django import forms

class SerieFormulario(forms.Form):
    nombre=forms.CharField()
    año=forms.IntegerField()
    temporadas=forms.IntegerField()

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    año = forms.IntegerField()
    director = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=30)
    duracion = forms.FloatField()