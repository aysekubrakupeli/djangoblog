from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def blogposts(request):
    posts = Post.objects.all()
    return render (request, "blogposts.html", {"posts": posts})

def viewpost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "viewpost.html", {"post": post})

def newpost(request):
    form = BlogPostForm()
    return render(request, 'newpost.html', {'form': form})

