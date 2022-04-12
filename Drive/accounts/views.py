from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_user
from .models import *
from .forms import OrderForm,CreateUserForm
# Create your views here.
def loginPage(request):
  
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  

        user = authenticate(request,username = username,password= password) 
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Username or Password is incorrecct')
            return render(request,'accounts/login.html')

    
    return render(request,'accounts/login.html')
def logoutUser(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.user.is_authenticated:
        return redirect('')
    else:    
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+user)
                return redirect('/login')
                
        context = {'form':form}
   
        return render(request,'accounts/register.html',context) 

def home(request):
   
     return render(request,'accounts/home.html')

def lesson(request):
    return render(request,'accounts/lesson.html')

def contact(request):
   
    return render(request,'accounts/contact.html')


  
@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/admin/products.html',{'products':products})

@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
def dashboard(request):
    
    booking = Booking.objects.all()
    

    context = {'booking':booking,}

    return render(request,'accounts/admin/dashboard.html',context)  


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
def createorder(request):
    form = OrderForm()
    if request.method =='POST':
        print('Printing POst:',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form':form}
    return render (request,'accounts/admin/order_form.html',context)  
@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
def update_order(request,pk):
    order = Booking.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')


    context = {'form':form}
    return render (request,'accounts/admin/order_form.html',context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
def delete_order(request ,pk):
     order = Booking.objects.get(id=pk)
     if request.method == "POST":
         order.delete()
         return redirect('/dashboard')
     context = {'item':order}
     return render(request,'accounts/admin/delete.html',context)

@login_required(login_url="/login")
def booking(request):
    return render(request,'accounts/booking.html')


def submit(request):
    name = request.POST['name']
    phone = request.POST['phone']
    vehicle = request.POST['vehicle']
    date1 = request.POST['date1']
    time1 = request.POST['time1']
    addbooking = Booking(user=name,Product=vehicle,date=date1,time=time1,phone=phone)
    addbooking.save()
    messages.success(request,'Data saved')
    return redirect("/bookingdash")

def bookingdash(request):
    return render(request,'accounts/bookingdash.html')

