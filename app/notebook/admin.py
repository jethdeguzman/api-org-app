from django.contrib import admin
from .models import Notebook, Note

class NoteInline(admin.TabularInline):
    model = Note
    fields = ('title', 'text', 'date_created', 'date_updated')
    readonly_fields = ('date_created', 'date_updated')
    extra = 1

class NotebookAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated',)
    readonly_fields = ('date_created', 'date_updated')
    inlines = (NoteInline,)

admin.site.register(Notebook, NotebookAdmin)
