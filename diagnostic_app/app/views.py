from django.shortcuts import render
from django.urls import reverse

def home(request):
  
    return render(request, 'app/home.html', {'title': 'Home'})

def patient(request):
    return render(request, 'app/patient_data.html', {'title': 'Patient Data'})

