from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.index),
    path('<int:ars_id>/<int:route>/', views.predict_output),
]