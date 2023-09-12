from django.shortcuts import render
from django.http import HttpResponse

from .models import ContactForm
from django.http import HttpResponse
# Create your views here.
def hi(request): 
    if request.method == "POST":
        contact=ContactForm()
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        age=request.POST.get("age")

        contact.firstname = firstname
        contact.lastname=lastname
        contact.email=email
        contact.phone=phone
        contact.age=age
        contact.save()
        return HttpResponse("<h1>Thank you for submit</h1>")
    return render(request, 'hi.html')