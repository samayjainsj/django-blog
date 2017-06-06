from django.shortcuts import render
from posts.models import Post


def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'mainpages/index.html', context)


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'mainpages/blog.html', context)


def about(request):
    return render(request, 'mainpages/about.html')


def contact(request):
    return render(request, 'mainpages/contact.html')
