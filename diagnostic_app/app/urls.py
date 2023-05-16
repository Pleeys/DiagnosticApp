from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('patient/', views.patient, name='app-patient'),
    path('symptoms/', views.symptoms, name='app-symptoms'),
    path('results/', views.results, name='app-results'),
    path('comments/', views.comments, name='app-comments'),
    path('register/', user_views.register, name='app-register'),
    path('login/', user_views.login, name='app-login'),
]
