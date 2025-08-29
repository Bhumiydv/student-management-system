from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    error=''
    if request.method == "POST":
        u=request.POST['uname']
        p=request.POST['pswd']
        admin=auth.authenticate(username=u,password=p)
        try:
            if admin.is_staff:
                auth.login(request,admin)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,"login.html",d)

@login_required(login_url='login')
def admin_home(request):
    return render(request,"admin_dashboard.html")

@login_required(login_url='login')
def add_student(request):
    error=''
    if request.method == "POST":
        n=request.POST['fname']
        e=request.POST['email']
        ph=request.POST['phone']
        cl=request.POST['college']
        city=request.POST['city']
        jd=request.POST['jdate']
        tf=request.POST['tfee']
        pf=request.POST['pfee']
        lf=request.POST['lfee']
        tech=request.POST['technology']
        img=request.FILES['image']
        try:
            student.objects.create(name=n,email=e,phone=ph,college=cl,city=city,jdate=jd,tfee=tf,pfee=pf,lfee=lf,technology=tech,image=img)
            error='no'
        except:
            error='yes'
    d={'error':error}
    return render(request,"add_student.html",d)

@login_required(login_url='login')
def view_students(request):
    data= student.objects.all()
    d={'data':data}
    return render(request,"view_students.html",d)

@login_required(login_url='login')
def edit_students(request,id):
    data=student.objects.get(id=id)
    error=''
    if request.method == "POST":
        n=request.POST['fname']
        e=request.POST['email']
        ph=request.POST['phone']
        cl=request.POST['college']
        city=request.POST['city']
        jd=request.POST['jdate']
        tf=request.POST['tfee']
        pf=request.POST['pfee']
        lf=request.POST['lfee']
        tech=request.POST['technology']
        img=request.FILES['img']

        data.name=n
        data.email=e
        data.phone=ph
        data.college=cl
        data.city=city
        data.jdate=jd
        data.tfee=tf
        data.pfee=pf
        data.lfee=lf
        data.technology=tech
        data.image=img
        try:
            data.save()
            error='no'
        except:
            error='yes'    
    d={'data':data, 'error':error}
    return render(request,"edit_students.html",d)

def contact(request):
    error=""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        d = request.POST['description']
        try:
            contactus.objects.create(full_name=f,last_name=l,email=e,description=d)
            error = "no"
        except:
            error = "yes"
    s={'error':error}
    return render(request,"contact.html",s)

@login_required(login_url='login')
def del_students(request,id):
    if request.method == "POST":
        data=student.objects.get(id=id)
        data.delete()
    return redirect("view_students")

@login_required(login_url='login')
def search_data(request):
    return render(request,"search.html")

@login_required(login_url='login')
def search_stu(request):
    n=request.POST['sname']
    data=student.objects.filter(name__icontains=n)
    d={'data':data}
    return render(request,'view_students.html',d)

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def change_pass(request):
    if request.method == "POST":
        op=request.POST['cp']
        np=request.POST['np']
        user=request.user
        if not user.check_password(op):
            return redirect('change_pass')
        user.set_password(np)
        user.save()
    return redirect('login')

def account(request):
    return render(request,'account.html')