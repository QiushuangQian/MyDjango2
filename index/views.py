from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .form import *

def index(request):
    product = ProductForm()
    return render(request,'data_form.html',locals())