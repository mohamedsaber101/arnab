from django import forms
from operation.models import *


class NewArnabaForm(forms.ModelForm):
    class Meta():
        model = Arnaba
        fields = '__all__'


class NewArnabForm(forms.ModelForm):
    class Meta():
        model = Arnab
        fields = '__all__'