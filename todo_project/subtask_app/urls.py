from django.urls import path
from . import views
from todo_app.models import Todos


  
urlpatterns = [
    path('createTask/<Todos_id>', views.createTask, name='createTask'),
    path('detailTask/<Todos_id>', views.detailTask, name='detailTask'),
    path('delete/<Subtask_id>', views.delete, name ="deleteTask"),
    path('yes_finish/<Subtask_id>', views.yes_finish, name ="yes_finishTask"),
    path('no_finish/<Subtask_id>', views.no_finish, name ="no_finishTask"),
    path('update/<Subtask_id>', views.update, name ="updateTask"),
    
    
        
]
