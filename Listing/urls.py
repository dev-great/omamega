# property_listings/urls.py

from django.urls import path
from .views import estate_listing_list, property_listing_list, property_listing_detail

app_name = 'Listing'
urlpatterns = [
    path('estate-listings/', estate_listing_list,
         name='estate_listing_list'),
    path('property-listings/', property_listing_list,
         name='property_listing_list'),
    path('property-listings/<int:pk>/', property_listing_detail,
         name='property_listing_detail'),
]
