from django.urls import path
from . import views
from todo_app.models import Todos


  
urlpatterns = [
    path('createTask/<Todos_id>', views.createTask, name='createTask'),
    path('detailTask/<Todos_id>', views.detailTask, name='detailTask'),
    
    

    
]

'''
    path('<int:Todos_id>/update/<int:Subtask_id>', views.update, name='update'),
    path('<int:Todos_id>/delete/<int:Subtask_id>', views.delete, name='delete'),
    path('<int:Todos_id>/yes_finish/<int:Subtask_id>', views.yes_finish, name='yes_finish'),
    path('<int:Todos_id>/no_finish/<int:Subtask_id>', views.no_finish, name='no_finish'),
    path('<int:Todos_id>/completed_todos', views.completed_todos, name='completed_todos'),
    path('<int:Todos_id>/uncompleted_todos', views.uncompleted_todos, name='uncompleted_todos'),
'''