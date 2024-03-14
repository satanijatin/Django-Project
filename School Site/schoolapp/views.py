from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def login(request):
    if request.method=="POST":
        emailone = request.POST['email']
        password = request.POST['password']
        try:
            select_user = principal_login.objects.get(email=emailone)
            
            if select_user.password == password:
                request.session['email'] = select_user.email
                request.session['is_login'] = True
                role = request.POST['role']
               
                if select_user.role == role == "admin":
                    request.session['user_role'] = "admin"
                    return redirect('dashboard')
                elif select_user.role == role and role == "teacher":
                    request.session['user_role'] = "teacher"
                    return redirect('dashboard')
                elif select_user.role ==role and role == "student":
                    request.session['user_role'] = "student"
                    return redirect('dashboard')
                else:
                 return render(request,"login.html",{"msg":"Wrong Role Pass"}) 
            else:
                return render(request,"login.html",{"msg":"Wrong password"})         
        except:
                  
            return render(request,"login.html",{"msg":"Wrong email id or password"})
    else:
        try:
            if request.session['is_login']==True:
                return redirect('dashboard')
        except:
            return render(request,"login.html")

def isLogin(request):
     if request.session.get('is_login',False)==False:
         return False
     else:
         return True
     
def dashboard(request):
       
    if isLogin(request)==False:
        return redirect('login')
    
    if request.session.get('user_role','none')== "admin":
        return render(request,"index.html")
    elif request.session.get('user_role','none')== "teacher":
        return render(request,"teacherindex.html")
    elif request.session.get('user_role','none')== "student":
        return render(request,"studentindex.html")
  


def logout(request):
    del request.session['user_role']
    del request.session['email']
    del request.session['is_login']
    return redirect('login')