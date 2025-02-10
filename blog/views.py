from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


# Create your views here.
# 'request' is what we receive from the user when calling this function/method

def post_list(request):
    # Retrieve all the posts published before the current time and
    # order by published date.

    # Posts.objects.filter will return a QuerySet (table in other DBMS)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # render(request, HTML_template, data for template to use)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk);
    return render(request, 'blog/post_detail.html', {'post': post});