from django.shortcuts import render
from .models import Project, Contact

def home(request):
    return render(request, 'pages/home.html')

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'pages/projects.html', {'projects': projects})

def skills(request):
    return render(request, 'pages/skills.html')

def contact(request):
    contact_info = Contact.objects.first()
    return render(request, 'pages/contact.html', {'contact': contact_info}) 