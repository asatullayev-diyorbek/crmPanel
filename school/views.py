from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'base.html')

@login_required
def login(request):
    return render(request, 'auth/login.html')
