from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
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

def post_new(request):
    # PostForm is the HTML layout of the form itself

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user # This will be our username
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user # This will be our username
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {'form': form})