from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.index, name ="index"),
    path('create/', views.create, name ="create"),
    path('delete/<Todos_id>', views.delete, name ="delete"),
    path('yes_finish/<Todos_id>', views.yes_finish, name ="yes_finish"),
    path('no_finish/<Todos_id>', views.no_finish, name ="no_finish"),
    path('update/<Todos_id>', views.update, name ="update"),
    path('completed_todos/', views.completed_todos, name="completed_todos"),
    path("uncompleted_todos/", views.uncompleted_todos, name="uncompleted_todos"),

]

