from django import forms
from notebook.models import Note
from checklist.models import ChecklistItem

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['notebook', 'title', 'text']
        widgets = {
            'notebook': forms.Select(attrs={'class' : 'form-control', 'required' : 'required'}),
            'title': forms.TextInput(attrs={'class' : 'form-control notes-input-title', 'required' : 'required', 'placeholder' : 'Title', 'autocomplete':'off'}),
            'text': forms.Textarea(attrs={'class' : 'form-control notes-input-text', 'required' : 'required', 'placeholder' : 'Text', 'style' : 'height:320px;'})
        }

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ['checklist', 'title', 'done']
        widgets = {
            'checklist' : forms.Select(attrs={'class' : 'form-control', 'style' : 'display:none;'}),
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'required' : 'required', 'placeholder' : 'Title', 'autocomplete':'off'}),
            'done' : forms.CheckboxInput(attrs={'class' : 'flat'})
        }
