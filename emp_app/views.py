from datetime import datetime
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime


# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    print("hello")
    context = {

        'emps': emps 

    }
    return render(request,'view_all_emp.html',context)

'''def add_emp(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=request.POST['salary']
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role1 = Role.objects.create(name=request.POST['Role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,Role_id=role1,hire_date=datetime.now())
        
        new_emp.save()

        return HttpResponse("Employee add succesfully")
    elif request.method=="GET":
      return render(request,'add_emp.html')
    else:
        return HttpResponse("an exceptional occurred employee has not add" )  
'''
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("please enter valid emp id")    
    emps=Employee.objects.all()
    context = {
    'emps': emps

    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method =="POST":
        name=request.POST["first_name"]
        dept=request.POST["dept"]
        role=request.POST["role"]
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(first_name__icontains=name)
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(Role__name__icontains=role)
        context ={
            'emps':emps
        }    
        return render(request,"view_all_emp.html", context)
    elif request.method=="GET":   
        return render(request,'filter_emp.html')  
    else:
        return HttpResponse("Exceptional Occured")          
    

