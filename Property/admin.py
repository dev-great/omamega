from django.contrib import admin

from Property.models import Document, Property, PropertyImage, PropertyManager

# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_type', 'file', 'created_on', 'updated_on',)
    list_filter = ('document_type',)
    search_fields = ('document_type',)


admin.site.register(Document, DocumentAdmin)


class PropertyManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_information',
                    'created_on', 'updated_on',)
    search_fields = ('name',)


admin.site.register(PropertyManager, PropertyManagerAdmin)

admin.site.register(PropertyImage)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'property_type',
                    'num_bedrooms', 'num_bathrooms', 'property_manager', )
    list_filter = ('num_bedrooms', 'num_bathrooms',)
    search_fields = ('name', 'name', 'property_type', 'num_bedrooms',
                     'num_bathrooms', 'property_manager',)


admin.site.register(Property, PropertyAdmin)
