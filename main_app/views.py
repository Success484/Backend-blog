from django.shortcuts import render
from .models import Post, Category,Comment

# Create your views here.


def home_page(request):
    all_article = Post.objects.all()
    context = {
        "articles" : all_article
    }
    return render(request, 'main/index.html', context)


def single_blog(request, blog_id):
    post=Post.objects.get(id=blog_id)
    category=Category.objects.all()
    comment = Comment.objects.all()
    similar_post = Post.objects.filter(category = post.category).exclude(id = post.id)
    context = {
        "article" : post,
        "articles" : category,
        'similar' : similar_post,
        'coment' : comment,
    }
    return render(request, 'main/post.html', context)