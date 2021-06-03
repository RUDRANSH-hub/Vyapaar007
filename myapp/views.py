from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
 

       
        name=request.POST.get("name")
        email= request.POST.get("email")
        phone= request.POST.get("phone")
        zip= request.POST.get("zip")
        contact=Contact(name=name,email=email,phone=phone,zip=zip)
        contact.save()
        
    
    return render(request,'contact.html')

