from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ToDoCreateView,ToDoListView,ToDoUpdateView,ToDoDeleteView,clear_all

urlpatterns=[
    path('home/',login_required(ToDoListView.as_view()),name="home"),
    path('todo/new/',ToDoCreateView.as_view(),name="todo-create"),
    path('todo/<int:pk>/update',ToDoUpdateView.as_view(),name='todo-update'),
    path('todo/<int:pk>/delete',ToDoDeleteView.as_view(),name='todo-delete'),
    path('todo/clear_all/',clear_all,name="clear_all")
]
