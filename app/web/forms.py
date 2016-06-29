from django import forms
from notebook.models import Note
from checklist.models import ChecklistItem, Checklist

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

class NoteSwitchForm(forms.Form):
    checklists = forms.ChoiceField(label='Checklists', widget=forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Checklists', 'required' : 'required'}))

    def __init__(self, *args, **kwargs):
        self.checklists = None
        if 'checklists' in kwargs:
            self.checklists = kwargs.pop('checklists')
        super(NoteSwitchForm, self).__init__(*args, **kwargs)
        self.fields['checklists'].choices = self.checklists


class ChecklistItemSwitchForm(forms.Form):
    notebooks = forms.ChoiceField(label='Notebooks', widget=forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Checklists', 'required' : 'required'}))

    def __init__(self, *args, **kwargs):
        self.notebooks = None
        if 'notebooks' in kwargs:
            self.notebooks = kwargs.pop('notebooks')
        super(ChecklistItemSwitchForm, self).__init__(*args, **kwargs)
        self.fields['notebooks'].choices = self.notebooks

        