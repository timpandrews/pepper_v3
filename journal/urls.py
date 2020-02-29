from django.contrib import admin
from django.urls import path
from journal import views

urlpatterns = [
    path('journal/', views.journal, name='journal'),
    path('journal/<int:id>/', views.journal_detail, name='journal_detail'),
    path('journal/new/', views.journal_new, name='journal_new'),
    path('journal/<int:id>/edit/', views.journal_edit, name='journal_edit'),
    path('journal/<int:id>/delete/', views.journal_delete, name='journal_delete'),
    path('inventory/', views.inventory, name='inventory'),
]
