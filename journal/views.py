from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from journal.forms import JournalForm, PlantsForm
from journal.models import Journal, Plants

import logging
import logzero
from logzero import logger
logzero.loglevel(logging.INFO)

def journal(request):
   logger.info('journal')
   journals = Journal.objects.all()
   logger.info(f'Qty: {journals.count()}')
   context = {
      'journals': journals,
   }
   return render(request, 'journal.html', context)


def journal_detail(request, id):
   journal = get_object_or_404(Journal, id=id)
   context = {
      'journal': journal,
   }
   return render(request, 'journal_detail.html', context)


def journal_new(request):
   if request.method == "POST":
      form = JournalForm(request.POST)
      if form.is_valid():
         journal = form.save(commit=False)
         journal.author = request.user
         journal.save()
         return redirect('journal_detail', id=journal.id)
   else:
      form = JournalForm()

   context = {
      'form': form,
      'action': 'new',
   }
   return render(request, 'journal_edit.html', context)


def journal_edit(request, id):
   journal = get_object_or_404(Journal, id=id)
   if request.method == "POST":
      logger.info("post")
      form = JournalForm(request.POST, instance=journal)
      if form.is_valid():
         logger.info("valid")
         journal = form.save(commit=False)
         journal.author = request.user
         journal.save()
         return redirect('journal_detail', id=journal.id)
   else:
      form = JournalForm(instance=journal)

   context = {
      'form': form,
      'action': 'edit',
   }
   return render(request, 'journal_edit.html', context)


def journal_delete(request, id):
   logger.info("journal_delete")
   journal = get_object_or_404(Journal, id=id)
   if journal:
      journal.delete()
      # todo: delete confirmation message
      logger.info(f"delete journal {id}")
   journals = Journal.objects.all()
   context = {
      'journals': journals,
   }
   return render(request, 'journal.html', context)


def plants(request):
   logger.info('Plants')
   plants = Plants.objects.all()
   logger.info(f'Qty: {plants.count()}')
   context = {
      'plants': plants,
   }
   return render(request, 'plants.html', context)


def plants_detail(request, id):
   plants = get_object_or_404(Plants, id=id)
   context = {
      'plants': plants,
   }
   return render(request, 'plants_detail.html', context)


def plants_new(request):
   if request.method == "POST":
      form = PlantsForm(request.POST)
      if form.is_valid():
         plants = form.save(commit=False)
         plants.author = request.user
         plants.save()
         return redirect('plants_detail', id=plants.id)
   else:
      form = PlantsForm()

   context = {
      'form': form,
      'action': 'new',
   }
   return render(request, 'plants_edit.html', context)


def plants_edit(request, id):
   plants = get_object_or_404(Plants, id=id)
   if request.method == "POST":
      logger.info("post")
      form = PlantsForm(request.POST, instance=plants)
      if form.is_valid():
         logger.info("valid")
         plants = form.save(commit=False)
         plants.author = request.user
         plants.save()
         return redirect('plants_detail', id=plants.id)
   else:
      form = PlantsForm(instance=plants)

   context = {
      'form': form,
      'action': 'edit',
   }
   return render(request, 'plants_edit.html', context)


def plants_delete(request, id):
   logger.info("plants_delete")
   plants = get_object_or_404(Plants, id=id)
   if plants:
      plants.delete()
      # todo: delete confirmation message
      logger.info(f"delete plants {id}")
   plants = Plants.objects.all()
   context = {
      'plants': plants,
   }
   return render(request, 'plants.html', context)