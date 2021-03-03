from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "info/index.html")

def project(request):
    a = User.objects.get(username="birajad").list_project.all()
    descriptions = dict()
    for i in a:
        descriptions[i] = i.description.split(',')
    print("Description",descriptions)
    return render(request, "info/projects.html", {
        "projects": descriptions
    })

def contact(request):
    return render(request, "info/contact.html")