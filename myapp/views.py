from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get("check")
        if check is None:
            isActive = False
        else:
            pass
        print(check)

    date = datetime.datetime.now()
    name = "Rohan Prakasan"
    To_DO =[
        'LEARN MERN',
        'Revise Backend',
        'Again Learn MERN'
    ]
    student={
        'student_name':"Rohan Prakasan",
        'student_college':"SIES GST",
        'student_city':"Dombivli"
    }
    data={
        'date': date,
        'isActive':isActive,
        'To_Do': To_DO,
        'name':name,
        'student_data': student
    }
    return render(request,"home.html",data)
    # return HttpResponse('<strong> Home Page </strong>')

def about(request):
    return render(request,"about.html",{})
    # return HttpResponse('<strong><u> This is About Page </u></strong>')

def index(request):
    return render(request,"home.html",{})
    
    # return HttpResponse('<strong>This is index Page</strong>')

def services(request):
    return render(request,"services.html",{})
    # return HttpResponse('<strong>This is service Page</strong>')