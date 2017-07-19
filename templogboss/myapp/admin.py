from django.contrib import admin
from myapp.models import Node, Attribute, Record
# Register your models here.
class NodeAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Node._meta.fields]
admin.site.register(Node,NodeAdmin)
	

class AttributeAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Attribute._meta.fields]
admin.site.register(Attribute,AttributeAdmin)

class RecordAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Record._meta.fields]
admin.site.register(Record,RecordAdmin)	