from django.conf.urls import url
from .views import (IndexView, NoteCreateView, NoteUpdateView, NoteDeleteView, 
    ChecklistItemListView, ChecklistItemUpdateView, ChecklistItemDeleteView, 
    ChecklistItemCreateView, NoteSwitchView, ChecklistItemSwitchView) 

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note$', NoteCreateView.as_view(), name='note_create'),
    url(r'^note/(?P<pk>[0-9]+)/$', NoteUpdateView.as_view(), name="note_update"),
    url(r'^note/(?P<pk>[0-9]+)/delete$', NoteDeleteView.as_view(), name="note_delete"),
    url(r'^note/(?P<pk>[0-9]+)/switch$', NoteSwitchView.as_view(), name="note_switch"),
    url(r'^checklist/(?P<pk>[0-9]+)/item$', ChecklistItemListView.as_view(), name="checklist_item_list"),
    url(r'^checklist/(?P<pk>[0-9]+)/item/create$', ChecklistItemCreateView.as_view(), name="checklist_item_create"),
    url(r'^checklist_item/(?P<pk>[0-9]+)$', ChecklistItemUpdateView.as_view(), name="checklist_item_update"),
    url(r'^checklist_item/(?P<pk>[0-9]+)/delete$', ChecklistItemDeleteView.as_view(), name="checklist_item_delete"),
    url(r'^checklist_item/(?P<pk>[0-9]+)/switch$', ChecklistItemSwitchView.as_view(), name="checklist_item_switch")
]
