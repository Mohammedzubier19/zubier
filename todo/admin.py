from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class studentAdmin(admin.ModelAdmin):
    list_display = Todo.DisplayFields
    search_fields = Todo.SearchableFields
