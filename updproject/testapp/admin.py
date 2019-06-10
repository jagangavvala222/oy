from django.contrib import admin
from testapp.models import Document,ResumeDocument

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display=['id','description','document','uploaded_at']
admin.site.register(Document,DocumentAdmin)

class ResumeDocumentAdmin(admin.ModelAdmin):
    list_display=['document']
admin.site.register(ResumeDocument,ResumeDocumentAdmin)
