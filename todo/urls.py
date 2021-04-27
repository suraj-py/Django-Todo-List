from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add', views.addTask, name='add'),
    path('complete/<todo_id>', views.completeTask, name='complete'),
    path('delete', views.deleteTask, name='delete')
]
