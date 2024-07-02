from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from crmapp.models import Customer,Login,Enquiry
from customerapp.models import Response,Orders
from .models import Product
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust  = Customer.objects.count()
            order = Orders.objects.count()
            ord = Orders.objects.latest('emailaddress')
            buyd = ord.buydate[:10]
            comp = Response.objects.filter(responsetype='complaint').count()
            latest_complaint_response = Response.objects.filter(responsetype='complaint').latest('id')
            res = Response.objects.filter(responsetype='feedback').count()
            latestUser = Customer.objects.latest('emailaddress')
            reg = latestUser.regdate[:10]
            enq = Enquiry.objects.latest('emailaddress')
            return render(request,"adminhome.html",locals())
    except:
         return redirect("crmapp:login")

def logout(request):
    try:
        del request.session["adminid"]
        return redirect("crmapp:login") 
    except:
        return redirect("crmapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=Customer.objects.all()
            return render(request,"viewcustomers.html",locals())
    except:
        return redirect("crmapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def viewenquiries(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq = Enquiry.objects.all()
            return render(request,"viewenquiries.html",locals())    
    except:
        return redirect("crmapp:login")
    
def delenq(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("adminapp:viewenquiries")    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedbacks(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            res = Response.objects.filter(responsetype='feedback')
            return render(request,"viewfeedbacks.html",locals())
    except:
        return redirect("crmapp:login")
        
def delfeed(request, id):
    try:
        # Assuming 'id' is the primary key of the Response object
        Response.objects.get(id=id).delete()
        
    except Response.DoesNotExist:
        # Handle case where the response with the given id does not exist
        pass
    return redirect("adminapp:viewfeedbacks")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def viewcomplaints(request):
    try:
        if request.session["adminid"]!=None:
            adminid = request.session["adminid"]
            comp = Response.objects.filter(responsetype='complaint')
            return render(request,"viewcomplaints.html",locals())
    except:
        return redirect("crmapp:login")
    
def delcomp(request,id):
    try:
        # Assuming 'id' is the primary key of the Response object
        Response.objects.get(id=id).delete()
        
    except Response.DoesNotExist:
        # Handle case where the response with the given id does not exist
        pass
    return redirect("adminapp:viewcomplaints")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changeadminpassword(request):
    if request.method == "POST":
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        conpassword = request.POST.get('conpassword')

        try:
            admin = Login.objects.get(userid=request.session['adminid'])
            
            if admin.password != oldpassword:
                msg = "Old password is incorrect."
            elif oldpassword == newpassword:
                msg = "New password cannot be the same as the old password."
            elif newpassword != conpassword:
                msg = "New password and confirm password do not match."
            else:
                admin.password = newpassword
                admin.save()
                msg = "Password changed successfully."

        except Login.DoesNotExist:
            msg = "Admin user does not exist."
        
        return render(request, "changeadminpassword.html", {'msg': msg})

    return render(request, 'changeadminpassword.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product(request):
    # try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            
            if request.method=="POST":
                productname=request.POST['productname']
                mfgdate=request.POST['mfgdate']
                expdate=request.POST['expdate']
                price=request.POST['price']
                productpic=request.FILES['productpic']
                prd = Product(productname=productname,mfgdate=mfgdate,expdate=expdate,price=price,productpic=productpic,avail='true')
                prd.save()
                msg = 'product is saved'
                
                return render(request,"product.html",locals())
            return render(request,"product.html",locals())
    # except:
        return redirect("crmapp:login")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewproducts(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            prod = Product.objects.all()
            return render(request,"viewproducts.html",locals())
    except:
        return redirect("crmapp:login")
    

def delp(request,id):
    try:
        # Assuming 'id' is the primary key of the Response object
        Product.objects.get(id=id).delete()
        
    except Product.DoesNotExist:
        # Handle case where the response with the given id does not exist
        pass
    return redirect("adminapp:viewproducts")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcustorders(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            ord = Orders.objects.all()
            return render(request,"viewcustorders.html",locals())
    except:
        return redirect("crmapp:login")