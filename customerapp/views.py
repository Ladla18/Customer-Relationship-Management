from django.shortcuts import render,redirect
from crmapp.models import Customer,Login
from .models import Response,Orders
from django.views.decorators.cache import cache_control
import datetime
from adminapp.models import Product
# from django.http import HttpResponseRedirect
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customerhome(request):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            ord = Orders.objects.filter(emailaddress=cust.emailaddress)
            return render(request,"customerhome.html",locals())
    except KeyError:
        return redirect('crmapp:login')  

def logout(request):
    try:
        del request.session["userid"]    
    except KeyError:
        return redirect('crmapp:login')
    return redirect('crmapp:login')
def response(request):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            if request.method=="POST":
                name=cust.name
                contactno=cust.contactno
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                responsetext=request.POST['responsetext']
                emailaddress = cust.emailaddress
                posteddate = datetime.datetime.today()
                res=Response(name=name,contactno=contactno,responsetype=responsetype,subject=subject,responsetext=responsetext,emailaddress=emailaddress,posteddate=posteddate)
                res.save()
                msg="Response is submitted"
                return render(request,"response.html",{"msg":msg})
            return render(request,"response.html") 
    except KeyError:
        return redirect('crmapp:login')
    return render(request,"response.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def changepassword(request):
    try:
        if request.session['userid']!=None:
            if request.method=="POST":
                cust = Login.objects.get(userid=request.session['userid'])
                oldpassword = request.POST['oldpassword']
                newpassword = request.POST['newpassword']
                conpassword = request.POST['conpassword']
                if cust.password == oldpassword:
                    if oldpassword==newpassword:
                        msg = "old password and new password are same"
                        return render(request,"changepassword.html",locals())
                    else:
                        if newpassword==conpassword:
                            cust.password=newpassword
                            cust.save()
                            msg = "Password Changes successfully"
                            return render(request,"changepassword.html",locals())
                        else:
                            msg  = "Confirm password didnt matched"
                            return render(request,"changepassword.html",locals())
                else:
                    msg = "Old Password is Wrong"
                    return render(request,"changepassword.html",locals())

            return render(request,'changepassword.html')
    except:
        return redirect('crmapp:login')    
    return render(request,'changepassword.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            if request.method=="POST":
                name = request.POST['name']
                gender = request.POST['gender']
                address = request.POST['address']
                emailaddress = request.POST['emailaddress']
                contactno = request.POST['contactno']
                Customer.objects.filter(emailaddress=emailaddress).update(name=name,gender=gender,address=address,contactno=contactno)
                msg = "Update Success"
                return render(request,"viewprofile.html",locals())
            return render(request,"viewprofile.html",locals())
            
    except KeyError:
        return redirect('crmapp:login')
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def products(request):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            prod = Product.objects.filter(avail='true')
            return render(request,"products.html",locals())
    except KeyError:
        return redirect('crmapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def buy(request,id):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            prod = Product.objects.get(id=id)
            productname = prod.productname
            price = prod.price
            name = cust.name
            contactno = cust.contactno
            emailaddress = cust.emailaddress
            productpic = prod.productpic
            buydate = datetime.datetime.today()
            ord = Orders(productname=productname,price=price,name=name,contactno=contactno,emailaddress=emailaddress,buydate=buydate,prodpic=productpic)
            ord.save()
            Product.objects.filter(id=id).update(avail='false')
            return redirect('customerapp:vieworders')
    except KeyError:
        return redirect('crmapp:login')  
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def vieworders(request):
    try:
        if request.session["userid"]!=None:
            cust = Customer.objects.get(emailaddress=request.session["userid"])
            ord = Orders.objects.filter(emailaddress=cust.emailaddress)
            return render(request,"vieworders.html",locals())
    except KeyError:
        return redirect('crmapp:login')  
