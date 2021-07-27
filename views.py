from django.shortcuts import render
from website.models import BookReview,Project

# Create your views here.

def cover(request):
    return render(request,'cover.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def projects(request):
    projects = Project.objects.all()
    url = str(Project.image).replace('static','')
    context = {
        'projects' : projects, 'url':url
    }
    return render(request,'projects.html',context)

def bookreviews(request):
    bookreviews = BookReview.objects.all()
    url = str(BookReview.image).replace('static','')
    context = {
        'bookreviews' : bookreviews, 'url':url
    }
    return render(request,'bookreviews.html',context)

