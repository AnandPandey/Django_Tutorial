from django.shortcuts import render

# Create your views here.
def all_project(request):
    return render(request,'project1/all_project.html')