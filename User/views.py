from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
# Create your views here.
def home_view (request):
    return render(request,'User/homepage.html')

def complaint_form_view(request):
    form = Crime_info_form()
    if request.method =="POST":
        form = Crime_info_form(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')
    context={
        'form':form
    }
    return render(request,'User/complaintpage.html',context)
