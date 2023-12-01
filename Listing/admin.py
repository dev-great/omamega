from django.contrib import admin

from Listing.models import PropertyListing

# Register your models here.


class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ('property',  'rental_price',
                    'selling_price', 'asking_price', 'is_published')
    search_fields = ('property',)


admin.site.register(PropertyListing, PropertyListingAdmin)
