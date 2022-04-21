from django.contrib import admin

from .models import Setting
# Register your models here.

# admin.site.register(Setting)

class SettingAdmin(admin.ModelAdmin):
    # ...
    list_display = ('user', 'app', 'configkey', 'configvalue')

admin.site.register(Setting, SettingAdmin)