from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('patient/', views.patient, name='app-patient'),
    path('symptoms/', views.symptoms, name='app-symptoms'),
    path('results/', views.results, name='app-results'),
    path('comments/', views.comments, name='app-comments'),
    path('register/', views.register, name='app-register'),
    path('login/', views.login, name='app-login'),
]
