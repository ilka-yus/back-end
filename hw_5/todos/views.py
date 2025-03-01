from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

def redirect_to_todo_lists(request):
    return redirect('todo_lists')

def redirect_to_login(request):
    return redirect('login')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'todos/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_list.html', {'todos': todos, 'form': form})

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    editable = request.user == todo.user or request.user.is_superuser
    return render(request, 'todos/todo_detail.html', {'todo': todo, 'editable': editable})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo_list')

@login_required
def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', id=todo.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})