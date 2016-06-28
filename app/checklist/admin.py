from django.contrib import admin
from .models import Checklist, ChecklistItem

class ChecklistItemsInline(admin.TabularInline):
    model = ChecklistItem
    fields = ('title', 'done', 'date_created', 'date_updated')
    readonly_fields = ('date_created', 'date_updated')
    extra = 1

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated',)
    readonly_fields = ('date_created', 'date_updated')
    inlines = (ChecklistItemsInline,)

admin.site.register(Checklist, ChecklistAdmin)
