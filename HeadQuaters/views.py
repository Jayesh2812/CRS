from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User , auth
from HeadQuaters.models import *
from .forms import Case_status
from django.forms.models import modelformset_factory
from User.forms import Crime_info_form
from django.core.exceptions import ValidationError

# Create your views here.
def HQlogin(request):
    context={}
    pass
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('reports')
        else:
            messages.info(request,'invalid credentials')
            return redirect('HQlogin')

    return render(request,'HQ/login.html',context)

def HQlogout(request):
    auth.logout(request)
    return redirect('home')

def reports_manage_view(request):
    obj = Maindb.objects.all()
    Manageformset=modelformset_factory(Maindb , form=Case_status,extra=0)

    formset = Manageformset(request.POST or None)
    if formset.is_valid():
        print("valid")
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save()
        return redirect('HQlogout')
    context={
        'obj':obj,
        'formset':formset,
        'objform':zip(obj,formset)
    }
    return render(request,'HQ/complaintmanage.html',context)