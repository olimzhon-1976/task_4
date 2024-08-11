from django.shortcuts import render
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Захватываем данные формы
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            subscribe_to_news = form.cleaned_data['subscribe_to_news']

            # Создание контекста для отображения данных
            return render(request, 'checkbox/registration_success.html', {
                'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'email': email,
                'gender': gender,
                'address': address,
                'subscribe_to_news': subscribe_to_news,
            })
    else:
        form = UserRegistrationForm()

    return render(request, 'checkbox/register.html', {'form': form})
