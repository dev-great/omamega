from django.shortcuts import render, get_object_or_404
from .models import PropertyListing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def property_listing_list(request):
    property_listings = PropertyListing.objects.filter(is_published=True)

    posts_per_page = 10
    paginator = Paginator(property_listings, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)
    context = {
        'listings': current_posts,
    }
    return render(request, 'listing/listings.html', context)


def estate_listing_list(request):
    property_listings = PropertyListing.objects.filter(
        is_published=True, property__is_estate=True)

    posts_per_page = 10
    paginator = Paginator(property_listings, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)
    context = {
        'listings': current_posts,
    }
    return render(request, 'listing/listings_estate.html', context)


def property_listing_detail(request, pk):
    property_listing = get_object_or_404(
        PropertyListing, pk=pk)
    context = {
        'listing': property_listing,
    }
    return render(request, 'listing/listings_details.html', context)
