from django.shortcuts import render, redirect
from .models import BlogPost

def blog_home(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            BlogPost.objects.create(title=title, content=content)
        return redirect("blog_home")
    return render(request, "blog/blog_home.html", {"posts": posts})


