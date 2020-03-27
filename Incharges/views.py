from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User , auth
from HeadQuaters.models import *

# Create your views here.
def login_view(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Ireports_view')
        else:
            messages.info(request,'invalid credentials')
            return redirect('Ilogin')

    return render(request,'Incharges/login.html',context)

def logout_view(request):
    auth.logout(request)
    return redirect('home')


def reports_view(request):
    obj = Maindb.objects.all() 
    if request.method == 'POST':
        print(request.POST)
        return redirect('Ilogout')
    print(list(obj))
    context={
        'obj' : obj
    }
    return render (request,'Incharges/complaintview.html',context)