from django.shortcuts import render, redirect
from .models import employedetails

# Create your views here.

def index(request):
    print ("welcome")
    return render(request,'HTML/index.html')

def create(request):
    print("create")
    forms_request =employedetails(name=request.POST['name'],email=request.POST['email'])
    forms_request.save()
    return redirect('/')
