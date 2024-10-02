from django.urls import path
from .views import index, create_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
