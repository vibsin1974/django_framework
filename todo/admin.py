from django.contrib import admin

from .models import todo
# Register your models here.

@admin.register(todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    
# admin.site.register(todo, TodoAdmin)
