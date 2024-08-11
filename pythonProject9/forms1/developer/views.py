from django.shortcuts import render
from .forms import YearForm
from datetime import datetime, timedelta

def get_developer_day(request):
    result = None
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            # Вычисляем дату 256-го дня в указанном году
            jan_first = datetime(year, 1, 1)
            developer_day = jan_first + timedelta(days=255)
            result = developer_day.strftime('%d %B (%A)')
    else:
        form = YearForm()

    return render(request, 'developer/developer_day.html', {'form': form, 'result': result})
