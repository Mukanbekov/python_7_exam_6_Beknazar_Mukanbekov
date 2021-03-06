from django.contrib import admin

# Register your models here.
from webapp.models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'created_at', 'updated_at']
    list_filter = ['name']
    search_fields = ['name', 'email']
    fields = ['id', 'name', 'email', 'text', 'status']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Books, BooksAdmin)
