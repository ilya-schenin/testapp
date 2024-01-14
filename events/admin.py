from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'img_preview']
    search_fields = ['title']
    list_filter = ["organization"]


admin.site.register(Event, EventAdmin)

