from django.conf.urls import url
from .views import IndexView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^note$', NoteCreateView.as_view(), name='note_create'),
    url(r'^note/(?P<pk>[0-9]+)/$', NoteUpdateView.as_view(), name="note_update"),
    url(r'^note/(?P<pk>[0-9]+)/delete$', NoteDeleteView.as_view(), name="note_delete"),
]

