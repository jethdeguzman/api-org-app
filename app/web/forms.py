from django import forms
from notebook.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['notebook', 'title', 'text']
        widgets = {
            'notebook': forms.Select(attrs={'class' : 'form-control', 'required' : 'required'}),
            'title': forms.TextInput(attrs={'class' : 'form-control notes-input-title', 'required' : 'required', 'placeholder' : 'Title', 'autocomplete':'off'}),
            'text': forms.Textarea(attrs={'class' : 'form-control notes-input-text', 'required' : 'required', 'placeholder' : 'Text', 'style' : 'height:320px;'})
        }
