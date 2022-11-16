from django import forms


class AutomovilesFormulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()
    año_de_fabricacion = forms.CharField()
    kilometraje = forms.CharField()


class MotosFormulario(forms.Form):
    
    marca = forms.CharField()
    modelo = forms.CharField()
    año_de_fabricacion = forms.CharField()
    kilometraje = forms.CharField()

class CamionetaFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    año_de_fabricacion = forms.CharField()
    kilometraje = forms.CharField()