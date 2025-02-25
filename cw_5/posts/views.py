from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Thread, Post
from .forms import ThreadForm, PostForm


def redirect_to_login(request):
    return redirect('login')

def redirect_to_thread(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()

    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread_form.save()
            return redirect('thread_list')
    else:
        thread_form = ThreadForm()

    return render(request, 'posts/thread_list.html', {'threads': threads, 'thread_form': thread_form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.thread = thread
            post.author = request.user
            post.save()
            return redirect('thread_detail', id=id)
    else:
        post_form = PostForm()

    return render(request, 'posts/thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})

@login_required
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

@login_required
def edit_thread(request, id):
    thread =get_object_or_404(Thread, id=id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=id)
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'posts/edit_thread.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponseForbidden("Вы не можете удалить этот пост")

    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponseForbidden("Вы не можете редактировать этот пост")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if form.cleaned_data.get('delete_picture'):
                post.picture = None
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('thread_list')
    return render(request, 'posts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)

    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('my_posts', id=id)
    else:
        post_form = PostForm()

    return render(request, 'posts/my_posts.html', {'posts': posts, 'post_form': post_form})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    editable = request.user == post.author or request.user.is_superuser
    return render(request, 'posts/post_detail.html', {'post': post, 'editable': editable})