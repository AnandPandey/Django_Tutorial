from django.shortcuts import render
from .models import projectVariety
from django.shortcuts import get_object_or_404
# Create your views here.
def all_project(request):
    projects = projectVariety.objects.all()
    return render(request,'project1/all_project.html', {'projects': projects})

def project_detail(request,project_id):
    project= get_object_or_404(projectVariety,pk= project_id)
    return render(request,'project1/project_detail.html',{'project':project})