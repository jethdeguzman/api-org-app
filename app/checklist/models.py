from __future__ import unicode_literals
import datetime
from django.db import models

class Checklist(models.Model):
    name = models.CharField(max_length=80, null=True, blank=False)
    date_created = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)
    date_updated = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        super(Checklist, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class ChecklistItem(models.Model):
    checklist = models.ForeignKey(Checklist, null=True, blank=False, related_name='items')
    title = models.CharField(max_length=80, null=True, blank=False)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)
    date_updated = models.DateTimeField(default=datetime.datetime.now, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        super(ChecklistItems, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
