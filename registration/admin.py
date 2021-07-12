from django.contrib import admin
from .models import Extended_User

class extended_user_admin(admin.ModelAdmin):
    list_display  = ('id','user', 'score',)
    
admin.site.register(Extended_User,extended_user_admin)
