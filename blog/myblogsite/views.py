from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 
                 'blogs/post/list.html',  # Changed to match your structure
                 {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    return render(request,
                 'blogs/post/detail.html',  # Changed to match your structure
                 {'post': post})