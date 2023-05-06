from django import forms
from operation.models import *


class NewArnabaForm(forms.ModelForm):
    class Meta():
        model = Arnaba
        fields = '__all__'
