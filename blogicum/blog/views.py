from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post


def index(request):
    template_name = "blog/index.html"
    post_list = Post.objects.all().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = "blog/detail.html"
    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = "blog/category.html"
    category = get_object_or_404(
        Category.objects.all().filter(slug=category_slug),
        is_published=True
    )
    post_list = Post.objects.all().filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template_name, context)
