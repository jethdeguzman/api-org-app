from rest_framework import serializers
from notebook.models import Notebook, Note
from checklist.models import Checklist, ChecklistItem

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note

class NotebookSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Notebook

class NotebookDetailSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Notebook
        fields = ('name', 'notes', 'date_created', 'date_updated')

class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem

class ChecklistSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Checklist

class ChecklistDetailSerializer(serializers.ModelSerializer):
    checklist_items = ChecklistItemSerializer(many=True, read_only=True)

    class Meta:
        model = Checklist
        fields = ('name', 'checklist_items', 'date_created', 'date_updated')
