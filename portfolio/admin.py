from django.contrib import admin
from .models import Project


@admin.register(Project)
class PorjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url')


