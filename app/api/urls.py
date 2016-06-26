from django.conf.urls import url
from .views import (NotebookList, NotebookDetail, NoteList, NoteDetail,
    ChecklistList, ChecklistDetail, ChecklistItemList, ChecklistItemDetail)

urlpatterns = [
    url(r'^notebook$', NotebookList.as_view()),
    url(r'^notebook/(?P<pk>[0-9]+)$', NotebookDetail.as_view()),
    url(r'^note$', NoteList.as_view()),
    url(r'^note/(?P<pk>[0-9]+)$', NoteDetail.as_view()),
    url(r'^checklist$', ChecklistList.as_view()),
    url(r'^checklist/(?P<pk>[0-9]+)$', ChecklistDetail.as_view()),
    url(r'^checklist_item$', ChecklistItemList.as_view()),
    url(r'^checklist_item/(?P<pk>[0-9]+)$', ChecklistItemDetail.as_view()),
]
