from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import (View, FormView, DetailView, ListView, 
    DeleteView, UpdateView, CreateView)
from .forms import NoteForm, ChecklistItemForm
from notebook.models import Note, Notebook
from checklist.models import Checklist, ChecklistItem

class BaseView(View):
    def get_checklist_url(self):
        checklist_url = '/'
        checklist = Checklist.objects.first()
        if checklist:
            checklist_url = reverse('checklist_item_view', kwargs={'pk' : checklist.pk })

        return checklist_url

class IndexView(BaseView):
    def get(self, request):
        context = {}
        context['checklist_url'] = self.get_checklist_url
        
        return render(request, 'web/index.html', context)

class BaseNoteView(BaseView):
    def get_context_data(self, **kwargs):
        context = super(BaseNoteView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all().order_by('-date_updated')
        context['checklist_url'] = self.get_checklist_url
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

            messages.add_message(self.request, messages.SUCCESS, 'Note is successfully updated.')
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

class ChecklistItemListView(BaseView, DetailView):
    context_object_name = 'checklist'
    model = Checklist
    template_name = 'web/checklist_item/list.html'

    def get_context_data(self, **kwargs):
        context = super(ChecklistItemListView, self).get_context_data(**kwargs)
        context['checklists'] = Checklist.objects.all()
        context['checklist_items'] = [{ 
            'data' : item, 
            'form' : ChecklistItemForm(
                initial={
                    'checklist' : item.checklist, 
                    'title' : item.title, 
                    'done' : item.done
                }
            )} for item in self.get_object().items.all().order_by('-date_created')]
        return context

class ChecklistItemUpdateView(BaseView, UpdateView):
    model = ChecklistItem
    fields = ['title', 'done']
    template_name = 'web/checklist_item/list.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Checklist Item is successfully updated.')
        return reverse('checklist_item_view', kwargs={'pk' : self.get_object().checklist.pk })

class ChecklistItemDeleteView(BaseView, DeleteView):
    model = ChecklistItem

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Checklist Item is successfully deleted.')
        return reverse('checklist_item_view', kwargs={'pk' : self.get_object().checklist.pk })

class ChecklistItemCreateView(BaseView):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        checklist = Checklist.objects.get(pk=self.kwargs.get('pk'))
        data = {'checklist': checklist, 'title' : title, 'done' : False}
        
        try:
            ChecklistItem.objects.create(**data)
            messages.add_message(self.request, messages.SUCCESS, 'Checklist item is successfully created.')
        except Exception:
            messages.add_message(self.request, messages.ERROR, 'Failed to create Checklist item.')

        return redirect(reverse('checklist_item_view', kwargs={'pk' : self.kwargs.get('pk') }))
