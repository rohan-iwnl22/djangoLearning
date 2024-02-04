from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp
from .models import Testimonial
# Create your views here.

def emp_home(request):
    emps = Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method == "POST":
        # fetch the data
        emp_name = request.POST.get("emp_name")
        emp_mail = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_ph")
        emp_address = request.POST.get("emp_add")
        working_status = request.POST.get("emp_working")
        emp_dep = request.POST.get("emp_dept")
        
        # create object model and set the data
        e = Emp()
        e.name = emp_name
        e.email = emp_mail
        e.phone = emp_phone
        e.address = emp_address
        if working_status is None:
            e.working = False
        else:
            e.working = working_status
        e.department = emp_dep

        # save the object
        e.save()
        # prepare message

        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def del_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')


def update_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp,
    })

def do_update_emp(request,emp_id):
    if request.method == "POST":
        
        emp_name = request.POST.get("emp_name")
        emp_mail = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_ph")
        emp_address = request.POST.get("emp_add")
        working_status = request.POST.get("emp_working")
        emp_dep = request.POST.get("emp_dept")

        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.email = emp_mail
        e.phone = emp_phone
        e.address = emp_address
        if working_status is None:
            e.working = False
        else:
            e.working = working_status

        e.department = emp_dep

        e.save()
    
    return redirect("/emp/home")

def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request,'emp/testimonials.html',{
        'testi' : testi,
    })