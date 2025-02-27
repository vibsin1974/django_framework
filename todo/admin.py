from django.contrib import admin

from .models import todo
# Register your models here.
admin.site.register(todo)

class TodoAdmin(admin.ModelAdmin):
    pass
