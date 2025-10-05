from django import forms

class CreateListForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=300)
