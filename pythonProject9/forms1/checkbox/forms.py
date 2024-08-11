from django import forms

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    age = forms.IntegerField(label='Возраст', min_value=1)
    email = forms.EmailField(label='Email')
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = forms.ChoiceField(label='Пол', choices=GENDER_CHOICES)
    address = forms.CharField(label='Адрес для доставки товара', max_length=255, widget=forms.Textarea)
    subscribe_to_news = forms.BooleanField(
        label='Хотите ли подписаться на новости нашего интернет-магазина?',
        required=False
    )