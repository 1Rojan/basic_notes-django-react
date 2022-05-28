from statistics import mode
from django.db import models

class Note(models.Model):
  body = models.TextField(null=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  crated_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.body[:50]
