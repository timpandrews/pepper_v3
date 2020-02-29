from django.http import HttpResponse
from django.shortcuts import render

from logzero import logger

def home(request):
   logger.info('home')
   logger.debug('home')
   logger.warning('home')
   logger.error('home')
   return render(request, '../templates/home.html', {})


