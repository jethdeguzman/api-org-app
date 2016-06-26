from __future__ import unicode_literals
import datetime
from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=80, null=True, blank=False)
    date_created = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)
    date_updated = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        super(Notebook, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Notes(models.Model):
    notebook = models.ForeignKey(Notebook, null=True, blank=False, related_name='notes')
    title = models.CharField(max_length=80, null=True, blank=False)
    text = models.TextField(null=True, blank=False)
    date_created = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)
    date_updated = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        super(Notes, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
        