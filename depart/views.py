from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from depart.models import Department, Project, Supervisor

# Create your views here.
def homepage(request): 
    return render(request, 'home.html')

def departmentPage(request):
    departments= Department.objects.all()
    
    return render(request, 'department.html', {'departments' : departments})

def addDepartmentPage(request):

    return render(request, 'department.html') 

def adddepartmentformsubmission(request):
    departments = get_object_or_404(Department)
    if request.method == 'POST':
        department_name = request.POST["department_name"]
        hod_name = request.POST["hod_name"]
        hod_phone_number = request.POST["hod_phone_number"]
        hod_email = request.POST["hod_email"]

        departments = Department.objects.create(department_name=department_name, hod_name=hod_name, hod_phone_number=hod_phone_number, hod_email=hod_email)

    return render(request, 'department.html', {'departments': departments})

def department_details(request, pk=None):
    departments= Department.objects.get(pk=pk)
    projects = Project.objects.all()
    supervisors = Supervisor.objects.all()
    context = {
        'departments': departments, 
        'projects':projects,
        'supervisors': supervisors
        } 
    return render(request, 'is.html', context )


