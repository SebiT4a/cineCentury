from django import forms
from mainApp.models import Funcion



class FormVenta(forms.Form):
    id_funcion = forms.CharField(widget=forms.HiddenInput)
    cliente = forms.CharField()
    email = forms.CharField(required=False)
    entradas = forms.IntegerField(min_value=1, max_value=10)
    codigo = forms.CharField(required=False)

    id_funcion.widget.attrs['class'] = 'form-control'
    cliente.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    entradas.widget.attrs['class'] = 'form-control'
    codigo.widget.attrs['class'] = 'form-control'

    def clean_entradas(self):
        id_funcion = self.cleaned_data['id_funcion']
        entradas = self.cleaned_data['entradas']
        funcion = Funcion.objects.get(id=id_funcion)

        if entradas > funcion.asientos_disponibles:
            raise forms.ValidationError("No hay tantas entradas disponibles")

        return entradas

