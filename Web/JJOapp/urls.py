from django.urls import path

from . import views

app_name = 'JJOapp'

urlpatterns = [
    path('main/', views.index, name='main'),
    path('detail/', views.predict_output, name='detail'),
]