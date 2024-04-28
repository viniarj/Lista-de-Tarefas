from django.urls import path
from . import views

urlpatterns = [
    path('ola/', views.ola, name='ola'),
    path('', views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
    path('newtask/', views.newTask, name="new-view"),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
    path('task/<int:id>',views.taskView, name='task-view'),
]