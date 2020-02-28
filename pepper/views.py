from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request, '../templates/home.html', {})

def journal(request):
   return HttpResponse('Journal!!')

def inventory(request):
   return HttpResponse('Inventory!!')
