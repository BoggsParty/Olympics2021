from django.contrib import admin
from .models import Comments, Responses

class Comments_admin(admin.ModelAdmin):
    list_display = ('user', 'date',)
    
admin.site.register(Comments, Comments_admin)

class Responses_admin(admin.ModelAdmin):
    list_display = ('user', 'date',)
    
admin.site.register(Responses, Responses_admin)