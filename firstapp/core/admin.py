from django.contrib import admin
from .models import *


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create', 'time_do', 'is_completed', 'color_id')
    search_fields = ('title', )
    list_editable = ('is_completed', )
    list_filter = ('time_do', 'is_completed', 'color_id')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ru_name')
    search_fields = ('name', 'ru_name')


admin.site.register(Note, NoteAdmin)
admin.site.register(Color, ColorAdmin)
