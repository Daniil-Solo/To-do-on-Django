from math import ceil
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Note, Color
from .forms import *

MAX_NOTES_ON_PAGES = 6
MAX_NUMBER_PAGES_ON_PAGE = 3


class NoteHome(ListView):
    model = Note
    template_name = 'core/home.html'
    context_object_name = "notes"

    def get_queryset(self):
        return self.model.objects.filter(is_completed=False)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['n_notes'] = len(context["notes"])
        return context

    def post(self, request, *args, **kwargs):
        note_id = request.POST.get('note')
        note = Note.objects.get(pk=note_id)
        note.is_completed = 1
        note.save()
        return redirect('home', permanent=True)


class NoteArchive(ListView):
    model = Note
    template_name = 'core/archive.html'
    context_object_name = "notes"
    paginate_by = 6

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NoteNew(CreateView):
    form_class = NewNoteForm
    template_name = 'core/new_note.html'
    success_url = reverse_lazy('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
