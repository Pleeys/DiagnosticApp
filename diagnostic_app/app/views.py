from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html', {'title': 'Home'})

def patient(request):
    return render(request, 'app/patient_data.html', {'title': 'Patient Data'})

def symptoms(request):
    return render(request, 'app/symptoms.html', {'title': 'Symptoms'})

def results(request):
    return render(request, 'app/results.html', {'title': 'Results'})

def comments(request):
    return render(request, 'app/comments.html', {'title': 'Comments'})

def register(request):
    return render(request, 'app/register.html', {'title': 'Register'})

def login(request):
    return render(request, 'app/login.html', {'title': 'Login'})
