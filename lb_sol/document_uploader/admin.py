from django.contrib import admin

from document_uploader.models import Document


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'document')
