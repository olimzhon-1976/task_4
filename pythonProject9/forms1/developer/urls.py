from django.urls import path
from .views import get_developer_day

urlpatterns = [
    path('', get_developer_day, name='developer_day'),
]