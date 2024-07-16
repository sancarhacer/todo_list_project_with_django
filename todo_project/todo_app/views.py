from django.shortcuts import render,redirect
from .models import Todos
from .forms  import ListForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
        if request.user.is_authenticated:
            if request.method == "POST":
                form = ListForm(request.POST or None)
                if form.is_valid:
                    form.save()
                    todo_list = Todos.objects.filter(user=request.user)
                    return render(request,"todo_app/index.html",{'todo_list': todo_list})
            else:
                todo_list = Todos.objects.filter(user=request.user)
                return render(request,"todo_app/index.html",{'todo_list': todo_list})
        else:
            return redirect('index')
        
@login_required
def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user  # Kullanıcıyı atan todos oluşturuluyor.
            new_todo.save()
            todo_list = Todos.objects.filter(user=request.user)
            return redirect('index')
    else:
        todo_list = Todos.objects.filter(user=request.user)
        return render(request, "todo_app/create.html", {'todo_list': todo_list})

def about(request):
    return render(request,"todo_app/about.html")

def delete(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.delete()
    return redirect("index")

def yes_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def no_finish(request,Todos_id):
    todo = Todos.objects.get(pk=Todos_id)
    todo.finished = True
    todo.save()
    return redirect("index")

def update(request,Todos_id):
    if request.method == "POST":
        todo_list = Todos.objects.get(pk=Todos_id)
        form = ListForm(request.POST or None, instance = todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")

    else:  

        todo_list = Todos.objects.all()
        return render(request,"todo_app/update.html",{'todo_list': todo_list})

@login_required
def completed_todos(request):
    completed_todos = Todos.objects.filter(finished=True,user=request.user)
    return render (request,"todo_app/completed.html",{"completed_todos": completed_todos})

@login_required
def uncompleted_todos(request):
    uncompleted_todos = Todos.objects.filter(finished=False,user=request.user)
    return render(request,"todo_app/uncompleted.html",{"uncompleted_todos": uncompleted_todos})
