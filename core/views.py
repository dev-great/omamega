from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone
from Blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Listing.models import PropertyListing
from MaintenanceRequest.models import MaintenanceRequest
from Property.models import Property
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Tenant.models import Tenant
from core.models import Testimonial, TrustedBrand

# Create your views here.


def index(request):
    listings = PropertyListing.objects.filter(property__is_estate=True)[:4]
    testimonials = Testimonial.objects.all()
    trusted = TrustedBrand.objects.all()
    posts = Post.objects.all()[:10]
    context = {
        'listings': listings,
        'posts': posts,
        'testimonials': testimonials,
        'trusted': trusted,
    }
    print(context)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='Authorization:login')
def dashboard(request):
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
    }
    print(user_details)
    properties = Property.objects.filter(landlord=request.user)
    # for property in properties:
    tenants = Property.tenants
    unpublished = properties.filter(is_published=False)
    expire = properties.filter(
        tenants__lease_agreement__lease_end_date__gt=timezone.now())
    published = properties.filter(is_published=True)
    maintainance = MaintenanceRequest.objects.filter(
        property__landlord=request.user)
    expire_date = Tenant.objects.all()

    context = {
        'user_details': user_details,
        'listings': properties,
        'repairs': maintainance,
        'unpublished': unpublished,
        'published': published,
        'tenants': tenants,
        'expire': expire,
    }
    return render(request, 'propsavy/dashboard.html', context)


@login_required(login_url='Authorization:login')
def my_properties(request):
    user = request.user
    properties = Property.objects.filter(landlord=request.user)
    posts_per_page = 20
    paginator = Paginator(properties, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)

    context = {
        'listings': current_posts,
        'isLandlord': user.is_Landlord,
    }
    print(context)
    return render(request, 'propsavy/pages/properties.html', context)


@login_required(login_url='Authorization:login')
def maintainance(request):
    return render(request, 'propsavy/pages/maintainance.html')


def account_type(request):
    return render(request, 'registration/account_type.html')


@login_required(login_url='Authorization:login')
def tenant(request):
    return render(request, 'propsavy/pages/tenant.html')


@login_required(login_url='Authorization:login')
def personal_info(request):
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
    }
    context = {
        'user_details': user_details,
    }
    return render(request, 'propsavy/pages/personal_info.html', context)


@login_required(login_url='Authorization:login')
def invoice(request):
    return render(request, 'propsavy/pages/invoice.html')
