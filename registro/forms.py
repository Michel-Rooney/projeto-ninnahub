from django import forms
from .models import Registro

class ParticipantesForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('participantes_presentes')