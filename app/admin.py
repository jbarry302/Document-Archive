from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file_document', 'document_url', 'picture', 'note')
    search_fields = ('title', 'description', 'note')
    ordering = ('title',)

admin.site.register(Document, DocumentAdmin)
