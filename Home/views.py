from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor,Booking
from .forms import BookingForms
#Create your views here
def index(request):
    #return httpresponse("Hello welcome")
    person={
        'name':'john',
        'age':30,
        'place':'Thrissur'
    }
    return render(request,"index.html",person)
def about(request):
    return render(request,"about.html",{'range':range(1,11)})
  #  return HttpResponse("About Us")
def show(request):
    number1={
        'num':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,"show.html",number1)
def hotel(request):
    return render(request,"hotel.html")
def department(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dic_dept)
def doctors(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"doctor.html",dic_doc)
def bookings(request):
    form=BookingForms()
    dic_form={
        'form':form
    }
    return render(request,"booking.html",dic_form)

