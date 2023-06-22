from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Attendance
# Create your views here.
#from django.utils.datastructures import MultiValueDict

def register(request):
    if request.method=="POST":
        username= request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user =User.objects.create_user (username=username,email=email,password=password)
        user.save()
        
        return redirect ("login_page")
    
    return render(request,"register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user =authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("attendance")
        else:
            error_message = "Username or password is incorrect. Please check your credentials and try again."
            return render(request,'login.html', {"error_message":error_message})
    return render(request,"login.html")
def attendance(request):
    if request.method == "POST":
        SelectClass = request.POST.get('SelectClass')
        RollNumbers = request.POST.getlist(SelectClass + '_roll_number[]')
        StudentNames = request.POST.getlist(SelectClass + '_student_name[]')
        DateTimes = request.POST.getlist(SelectClass + '_date_time[]')
        Attendances = request.POST.getlist(SelectClass + '_attendance[]')
        
        for i in range(len(RollNumbers)):
            attendance = Attendance(
                RollNumber=RollNumbers[i],
                StudentName=StudentNames[i],
                DateTime=DateTimes[i],
                Attendance=Attendances[i]
            )
            attendance.save()
    
    return render(request,"attendance.html")

def logout(request):
    
    return redirect("login_page")