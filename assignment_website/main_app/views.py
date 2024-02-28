from django.shortcuts import render
from .models import Post

# Create your views here.

def home_page_view(request):
    all_article=Post.objects.all()
    context={
        "articles":all_article
    }
    return render(request,"main/index.html", context)

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def single_blog_post(request, blog_id):
    post=Post.objects.get(id=blog_id)
    context={
        "article":post
    }
    return render(request, "main/post.html", context)
