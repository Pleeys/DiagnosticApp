from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('patient/', views.patient, name='app-patient'),
    path('symptoms/', views.symptoms, name='app-symptoms'),
]
