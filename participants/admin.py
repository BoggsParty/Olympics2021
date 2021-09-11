from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Guesses

class Guesses_admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user','sport','date','score')
    order = ('date')
    filter_by = ('sport','user')

admin.site.register(Guesses, Guesses_admin)