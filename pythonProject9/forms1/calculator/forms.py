from django import forms


class NumberForm(forms.Form):
    numbers = forms.CharField(label='Введите три числа через пробел', max_length=100)
    operation = forms.ChoiceField(
        choices=[
            ('min', 'Минимум'),
            ('max', 'Максимум'),
            ('avg', 'Среднеарифметическое')
        ],
        widget=forms.RadioSelect
    )