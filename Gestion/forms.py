from django import forms
from .models import asignaturas
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = asignaturas
        fields = "__all__"