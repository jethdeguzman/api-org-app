from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View, FormView, DetailView, ListView, DetailView, DeleteView
from .forms import NoteForm
from notebook.models import Note, Notebook

class BaseView(View):
    pass

class IndexView(BaseView):
    def get(self, request):
        context = {}
        context['notes'] = Note.objects.all().order_by('-id') 
        return render(request, 'web/index.html', context)

class BaseNoteView(BaseView):
    def get_context_data(self, **kwargs):
        context = super(BaseNoteView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all().order_by('-date_updated')
        return context

class NoteCreateView(BaseNoteView, FormView):
    template_name = "web/note/create.html"
    form_class = NoteForm

    def form_valid(self, form):
        data = form.cleaned_data

        try:
            Note.objects.create(**data)
            messages.add_message(self.request, messages.SUCCESS, 'Note successfully created.')
        except Exception:
            messages.add_message(self.request, messages.ERROR, 'Failed to create note.')

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('note_create')

class NoteUpdateView(BaseNoteView, DetailView, FormView):
    context_object_name = 'note'
    form_class = NoteForm
    model = Note
    template_name = 'web/note/update.html'

    def get_form_kwargs(self):
        kwargs = super(NoteUpdateView, self).get_form_kwargs()
        note = self.get_object()
        initial = {
            'notebook' : note.notebook,
            'title' : note.title,
            'text' : note.text
        }
        kwargs.update({'initial' : initial})
        return kwargs

    def form_valid(self, form):
        data = form.cleaned_data

        try:
            note = self.get_object()
            note.notebook = data['notebook']
            note.title = data['title']
            note.text = data['text']
            note.save()

            messages.add_message(self.request, messages.SUCCESS, 'Note successfully updated.')
        except Exception:
            messages.add_message(self.request, messages.ERROR, 'Failed to update note.')

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('note_update', kwargs={'pk' : self.get_object().pk })

class NoteDeleteView(DeleteView):
    model = Note

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Note successfully deleted.')
        return reverse('note_create')
