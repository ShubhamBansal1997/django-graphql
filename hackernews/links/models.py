from django.db import models

# Create your models here.

class Links(models.Model):
  url = models.URLField()
  description = models.TextField(blank=True)
