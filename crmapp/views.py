from django.shortcuts import render, redirect, reverse  # Importing functions for rendering templates and redirecting
import datetime  # Importing datetime module for handling dates and times
from .models import Enquiry, Customer, Login  # Importing models from the current directory
from django.core.exceptions import ObjectDoesNotExist  # Importing an exception class
from . smssender import sendsms
def index(request):
    return render(request, "index.html")  # Rendering the index.html template

def aboutus(request):
    return render(request, "aboutus.html")  # Rendering the aboutus.html template

def registration(request):
    if request.method == 'POST':  # Checking if the request method is POST
        # Getting form data from POST request
        name = request.POST['name']
        emailaddress = request.POST['emailaddress']
        contactno = request.POST['contactno']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        regdate = datetime.datetime.today()  # Getting current date and time
        usertype = 'customer'

        if password == conpassword:  # Checking if passwords match
            # Creating Customer and Login objects
            reg = Customer(name=name, emailaddress=emailaddress, contactno=contactno, gender=gender, address=address, regdate=regdate)
            login = Login(userid=emailaddress, password=password, usertype=usertype)
            reg.save()  # Saving Customer object to database
            login.save()  # Saving Login object to database

            # Redirecting to login page upon successful registration
            return redirect(reverse('crmapp:login'))
        else:
            return render(request, "registration.html", {'error': 'Password not matched'})  # Rendering registration.html template with error message

    return render(request, "registration.html")  # Rendering registration.html template

def login(request):
    if request.method == "POST":  # Checking if the request method is POST
        userid = request.POST['userid']
        password = request.POST['password']
        try:
            obj = Login.objects.get(userid=userid, password=password)  # Querying Login model for user
            if obj is not None:
                if obj.usertype == "customer":  # Checking if user is a customer
                    request.session["userid"] = userid  # Storing user session using user id
                    return redirect(reverse("customerapp:customerhome"))  # Redirecting to customer home page
                elif obj.usertype == "admin":  # Checking if user is an admin
                    request.session["adminid"]=userid
                    return redirect(reverse("adminapp:adminhome"))
        except ObjectDoesNotExist:
            msg = "Invalid User"  # Handling ObjectDoesNotExist exception
        return render(request, "login.html", {"msg": msg})  # Rendering login.html template with message

    return render(request, "login.html")  # Rendering login.html template

def contactus(request):
    if request.method == "POST":  # Checking if the request method is POST
        # Getting form data from POST request
        name = request.POST['name']
        contactno = request.POST['contactno']
        emailaddress = request.POST['emailaddress']
        subject = request.POST['subject']
        message = request.POST['message']
        posteddate = datetime.datetime.today()  # Getting current date and time

        # Creating Enquiry object and saving it to database
        enq = Enquiry(name=name, contactno=contactno, emailaddress=emailaddress, subject=subject, message=message, posteddate=posteddate)
        enq.save()
        sendsms(contactno)
        return render(request, "contactus.html", {"msg": "Enquiry is saved"})  # Rendering contactus.html template with success message

    return render(request, "contactus.html")  # Rendering contactus.html template

