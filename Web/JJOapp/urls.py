from django.urls import path

from . import views

app_name = 'JJOapp'

urlpatterns = [
    path('main/', views.index, name='main'),
    path('main/about_us', views.about, name='about-us'),
    path('detail/', views.detail, name='detail'),
    path('detail/<str:dist>+<str:station>+<str:route>/', views.info, name='info'),
]