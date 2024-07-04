from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

'''render:  HTML şablonlarını kullanıcıya sunmak için kullanılır'''
# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return render(request,"account/login.html",{"error": "Username or password is incorrect." })
    
    else:
        return render(request,"account/login.html")
def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        
        if password != repassword:
            return render(request, "account/register.html", {"error": "The password does not match."})
        
        # Kullanıcı adı ve e-posta kontrolü
        if User.objects.filter(username=username).exists():
            return render(request, "account/register.html", {"error": "This username has already been taken."})
        elif User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {"error": "This email address has already been registered."})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect("login")
    
    else:
        return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    return redirect("index")