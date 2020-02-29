from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from journal.forms import JournalForm
from journal.models import Journal

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
      'form': form
   }
   return render(request, 'journal_edit.html', context)


def journal_edit(request, id):
   journal = get_object_or_404(Journal, id=id)
   if request.method == "POST":
      form = JournalForm(request.POST, instance=journal)
      if form.is_valid():
         journal = form.save(commit=False)
         journal.author = request.user
         journal.save()
         return redirect('journal_detail', id=journal.id)
   else:
      form = JournalForm(instance=journal)

   context = {
      'form': form
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


def inventory(request):
   logger.info('inventory')
   context = {

   }
   return render(request, 'inventory.html', context)
