from django.contrib import admin

from .models import Dictionary
# Register your models here.

# Implements list_display at the admin interface
class DictionaryModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'description', 'search_count')

admin.site.register(Dictionary, DictionaryModelAdmin)