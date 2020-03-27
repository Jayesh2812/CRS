"""Crime_reporting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User.views import home_view,complaint_form_view
from Incharges.views import login_view,logout_view,reports_view
from HeadQuaters.views import reports_manage_view ,HQlogin,HQlogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('report-crime',complaint_form_view, name ='complaint_form'),
    path('logout',HQlogout),
    path('Incharges/login',login_view,name='Ilogin'),
    path('Incharges/logout',logout_view,name='Ilogout'),
    path('Incharges/view',reports_view,name='Ireports_view'),

    path('HQ/manage',reports_manage_view,name='reports'),
    path('HQ/login',HQlogin,name="HQlogin"),
    path('HQ/logout',HQlogout,name='HQlogout')
]

