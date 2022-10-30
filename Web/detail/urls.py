from django.urls import path

from . import views

app_name = 'detail'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('<str:dist>+<str:id_>+<str:route>/', views.info, name='info'),
]