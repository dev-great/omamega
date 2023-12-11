from django.core.mail import EmailMessage
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.utils import timezone
from Blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Listing.models import PropertyListing
from MaintenanceRequest.models import MaintenanceRequest
from Property.models import Property, Subscriber
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
    all_tenants = []

    # Iterate through each property and collect its tenants
    for property in properties:
        property_tenants = property.tenants.all()
        all_tenants.extend(property_tenants)

    tenants = all_tenants
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
    user = request.user
    if request.method == 'POST':
        maintainance_title = request.POST.get('maintainance_title')
        issue_description = request.POST.get('issue_description')
        image_attachment = request.FILES.get('image_attachment')

        # Send maintenance request email
        email = EmailMessage(
            'Propsavy Maintenance Request',
            f'Title: {maintainance_title}\nDescription: {issue_description}',
            'unique_mind16@yahoo.com',
            ['omamega@gmail.com'],
        )

        if image_attachment:
            email.attach(image_attachment.name,
                         image_attachment.read(), image_attachment.content_type)

        try:
            email.send()
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

        return HttpResponseRedirect('/success/')
    else:
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
        return render(request, 'propsavy/pages/maintainance.html', context)


def account_type(request):
    return render(request, 'registration/account_type.html')


@login_required(login_url='Authorization:login')
def subscriber(request):
    subscriber = Subscriber.objects.filter(user=request.user)
    context = {
        'subscribers': subscriber,
    }
    print(context)
    return render(request, 'propsavy/pages/subscriber.html', context)


@login_required(login_url='Authorization:login')
def tenant(request):
    user = request.user
    properties = Property.objects.filter(landlord=request.user)

    # Initialize an empty list to store all tenants associated with the properties
    all_tenants = []

    # Iterate through each property and collect its tenants
    for property in properties:
        property_tenants = property.tenants.all()
        all_tenants.extend(property_tenants)

    print(all_tenants)
    posts_per_page = 20
    paginator = Paginator(all_tenants, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)

    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
        'phone_number': user.phone_number,
        'address': user.address,
    }
    context = {
        'listings': current_posts,
        'user_details': user_details,
    }
    return render(request, 'propsavy/pages/tenant.html', context)


@login_required(login_url='Authorization:login')
def personal_info(request):
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
        'phone_number': user.phone_number,
        'address': user.address,
    }
    context = {
        'user_details': user_details,
    }
    return render(request, 'propsavy/pages/personal_info.html', context)


@login_required(login_url='Authorization:login')
def invoice(request):
    user = request.user
    user_details = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'isLandlord': user.is_Landlord,
        'phone_number': user.phone_number,
        'address': user.address,
    }
    property_lease_aggrement = Tenant.objects.filter(user=request.user)
    posts_per_page = 10
    paginator = Paginator(property_lease_aggrement, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)

    context = {
        'lease_aggrement': current_posts,
        'user_details': user_details,
        'clock': property_lease_aggrement.last,
    }
    return render(request, 'propsavy/pages/invoice.html', context)


def success(request):
    return render(request, 'thankyou.html')
