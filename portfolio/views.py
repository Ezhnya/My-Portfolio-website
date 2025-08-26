from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects_view(request):
    projects = Project.objects.all().order_by('-created_at') 
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    return render(request, "contact.html")
