from django import forms
from .models import PersonModel,PassportModel

class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonModel
        fields = "__all__"

class PassportForm(forms.ModelForm):
    class Meta:
        model = PassportModel
        fields = "__all__"

