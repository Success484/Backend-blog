from django.shortcuts import render
from .models import Post

# Create your views here.


def home_page(request):
    all_article = Post.objects.all()
    context = {
        "articles" : all_article
    }
    return render(request, 'main/index.html', context)


def single_blog(request, blog_id):
    post=Post.objects.get(id=blog_id)
    context = {
        "article" : post
    }
    return render(request, 'main/post.html', context)