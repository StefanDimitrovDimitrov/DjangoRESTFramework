from django.shortcuts import render, redirect

# Create your views here.
from Templates.todos.forms import TodoForm
from Templates.todos.models import Todo


def list_todos(request):
    context = {
        'todos': Todo.objects.all()
    }

    return render(request, 'todo/list_todos.html', context)


def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list todos')
        else:
            form = TodoForm()
    context = {
        'form': form,
    }

    return render(request, 'todo/create_todo.html', context)
