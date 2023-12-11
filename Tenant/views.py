from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def property_listing_list(request):
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
    }
    return render(request, 'propsavy/pages/invoice.html', context)
