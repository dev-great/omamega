from .models import Post, Tag, Category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request, tag=None, category=None):
    posts = Post.objects.all()

    if tag:
        tag_name = get_object_or_404(Tag, name=tag)
        posts = posts.filter(tags=tag_name)

    if category:
        category_name = get_object_or_404(Category, name=category)
        posts = posts.filter(categories=category_name)

    posts_per_page = 20
    paginator = Paginator(posts, posts_per_page)
    page = request.GET.get('page')

    try:
        current_posts = paginator.page(page)
    except PageNotAnInteger:
        current_posts = paginator.page(1)
    except EmptyPage:
        current_posts = paginator.page(paginator.num_pages)

    context = {
        'posts': current_posts,
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()

    context = {
        'post': post,
        'tags': tags,
        'categories': categories,
    }

    return render(request, 'blog/post_detail.html', context)
