from django.shortcuts import render
from .forms import NumberForm


def calculate(request):
    result = None
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            numbers = list(map(float, form.cleaned_data['numbers'].split()))
            if len(numbers) == 3:  # Убедитесь, что введены ровно три числа
                operation = form.cleaned_data['operation']
                if operation == 'min':
                    result = min(numbers)
                elif operation == 'max':
                    result = max(numbers)
                elif operation == 'avg':
                    result = sum(numbers) / len(numbers)
    else:
        form = NumberForm()
    return render(request, 'calculator/calculate.html', {'form': form, 'result': result})
