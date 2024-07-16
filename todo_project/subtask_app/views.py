from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from todo_app.models import Todos
from subtask_app.forms import SubtaskForm
from subtask_app.models import Subtask

# Create your views here.
#commit=False parametresi, Django'da formdan veritabanına kayıt yaparken kullanılan bir özelliktir. Bu parametre, formdan alınan verileri doğrudan veritabanına kaydetmek yerine, önce formu kaydetmeyi erteler. Böylece, formu daha sonra işlem yapmak üzere değiştirebilir veya üzerinde ek işlemler yapabilirsiniz.
@login_required
def detailTask(request,Todos_id):
    subtask_list = Subtask.objects.filter(todo_id = Todos_id)    
    return render(request,"subtask_app/subtaskList.html",{'subtask_list': subtask_list, 'Todos_id':Todos_id})


    
@login_required
def createTask(request,Todos_id):
    
    if request.method == "POST":
        form = SubtaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            finished = form.cleaned_data['finished']
            date = timezone.now()
            todo = Todos.objects.get(pk = Todos_id)
            Subtask.objects.create( todo = todo, title=title,description = description,finished = finished,date=date)
            subtask_list = Subtask.objects.filter(todo_id = Todos_id)    
            return render(request,"subtask_app/subtaskList.html",{'subtask_list': subtask_list, 'Todos_id':Todos_id})
            
    else:
        
        subtask_list = Subtask.objects.filter(todo_id = Todos_id)           
        return render(request,'subtask_app/create.html',{'subtask_list':subtask_list})
        
   
''' 
def createTask(request):
   
    
    if request.method == "POST":
        form = SubtaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            finished =  form.cleaned_data["finished"]
            date = form.cleaned_data["date"]
            todo_id = request.POSt['todo_id']
            

            
            
            subtask_list = Subtask.objects.filter(todo=todos_instance)
            return render(request, "subtask_app/create.html", {
                'subtask_list': subtask_list,
                'todos_instance' : todos_instance
                })
    else:
        subtask_list = Subtask.objects.filter(todo=todos_instance)
        return render(request, "subtask_app/create.html", {
            'subtask_list': subtask_list,
            'todos_instance' : todos_instance
            })

 


def delete(request,Todos_id,Subtask_id):
    print(Subtask_id)
    subtask = Subtask.objects.get(pk=Subtask_id)
    subtask.delete()
    return redirect("subtaskList")

def yes_finish(request,Todos_id,Subtask_id):
    subtask = Subtask.objects.get(pk=Subtask_id)
    subtask.finished = False
    subtask.save()
    return redirect("subtaskList")

def no_finish(request,Todos_id,Subtask_id):
    subtask = Subtask.objects.get(pk=Subtask_id)
    subtask.finished = True
    subtask.save()
    return redirect("subtaskList")

def update(request,Todos_id,Subtask_id):
    if request.method == "POST":
        subtask_list = Subtask.objects.get(pk=Subtask_id)
        form = SubtaskForm(request.POST or None, instance = subtask_list)
        if form.is_valid:
            form.save()
            return redirect("subtaskList")

    else:  

        subtask_list = Subtask.objects.all()
        return render(request,"subtask_app/update.html",{'subtask_list': subtask_list})


def completed_todos(request,Todos_id):
    completed_todos = Subtask.objects.filter(finished=True,user=Todos_id)
    return render (request,"subtask_app/completed.html",{"completed_todos": completed_todos})


def uncompleted_todos(request,Todos_id):
    uncompleted_todos = Subtask.objects.filter(finished=False,user=Todos_id)
    return render(request,"subtask_app/uncompleted.html",{"uncompleted_todos": uncompleted_todos})

'''


"""
POST VERİLERİ
{
    'todo': '1',  # İlişkili Todos nesnesinin id değeri
    'title': 'Some Title',
    'description': 'Some Description',
    'finished': 'on',  # Checkbox işaretliyse 'on' olur, değilse bu anahtar POST verilerinde yer almaz
    'date': '2024-07-12',  # Kullanıcının girdiği tarih
}
"""