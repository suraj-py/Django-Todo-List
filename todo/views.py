from django.shortcuts import render, redirect

from . models import Todo
from . forms import TodoForm

def todo(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


def addTask(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_task = Todo(task = request.POST['task'])
        new_task.save()
    return redirect('todo')

def completeTask(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todo')

def deleteTask(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo')


