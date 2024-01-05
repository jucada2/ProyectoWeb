from django import forms

# Create your forms here.
class ConsolaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30) #equivalente al str de Python
    empresa = forms.CharField(max_length=30)
    año = forms.IntegerField()
    fecha = forms.DateField()