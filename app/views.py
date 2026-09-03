from django.shortcuts import render
from django.contrib.auth.models import User

def app(request):
    return render(request, 'app.html')

# Create your views here.
