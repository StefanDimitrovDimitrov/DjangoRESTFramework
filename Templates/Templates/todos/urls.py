from django.urls import path

from Templates.todos.views import create_todo, list_todos

urlpatterns = [
    path('', list_todos, name='list todos'),
    path('create/', create_todo, name='create todo')
]