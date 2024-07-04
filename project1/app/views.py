from django.shortcuts import render,render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Student

# Create your views here.
def home(request):
    # return HttpResponse("welcome app urls")
    data={"name":"himanshi","age":"23" ,"quali":"B.tech" }
    return JsonResponse(data)
def register(request):
    return render(request, 'registration.html')


def home1(request):
    return redirect("https://www.amazon.in/")

def registerdata(request):
    # return
    print(request.method)
    print(request.POST)
    name= request.POST.get("name") # name is key here and this will come form registration form 
    password=request.POST.get("password") 
    contact=request.POST.get("contact") 
    date=request.POST.get("date_of_birth")
    print(name,password,contact,date) #variables are written 

    Student.objects.create(Name=name, Password=password, Contact=contact , Date=date)
    print("data save successfully")