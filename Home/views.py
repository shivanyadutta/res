from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("this is home")
    return render(request, 'index.html')
def About(request):
    return render(request, 'index1.html')
def Education(request):
    return render(request,'education.html')
def Experience(request):
    return render(request,'experience.html')
def Projects(request):
    return render(request, 'projects.html')
def contactt(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        desc= request.POST.get('desc')
        contact=Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent successfully.")
    return render(request,'contact.html')