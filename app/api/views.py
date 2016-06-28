from checklist.models import Checklist, ChecklistItem
from notebook.models import Notebook, Note
from .serializers import (NotebookSerializer, NotebookDetailSerializer, NoteSerializer,
    ChecklistSerializer, ChecklistDetailSerializer, ChecklistItemSerializer)
from rest_framework import generics, mixins

class BaseList(mixins.ListModelMixin, 
               mixins.CreateModelMixin, 
               generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BaseDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class NotebookList(BaseList):
    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()

class NotebookDetail(BaseDetail):
    serializer_class = NotebookDetailSerializer
    queryset = Notebook.objects.all()

class NoteList(BaseList):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class NoteDetail(BaseDetail):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class ChecklistList(BaseList):
    serializer_class = ChecklistSerializer
    queryset = Checklist.objects.all()

class ChecklistDetail(BaseDetail):
    serializer_class = ChecklistDetailSerializer
    queryset = Checklist.objects.all()

class ChecklistItemList(BaseList):
    serializer_class = ChecklistItemSerializer
    queryset = ChecklistItem.objects.all()

class ChecklistItemDetail(BaseDetail):
    serializer_class = ChecklistItemSerializer
    queryset = ChecklistItem.objects.all()
    