from django.db import models
from organization.models import Organization
from django.utils.html import mark_safe

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    organization = models.ManyToManyField(Organization)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')