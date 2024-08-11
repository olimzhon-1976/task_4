from django import forms

class YearForm(forms.Form):
    year = forms.IntegerField(label='Введите год', min_value=1)