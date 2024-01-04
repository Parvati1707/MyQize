from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.

Login_Page_Link="validation/Login_Page.html"
Register_Page_Link="validation/Register_Page.html"
User_Profile_Page_Link="validation/User_Profile_Page.html"

def index(request):
    return render(request, 'index.html')


def register_page(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect(login_view)
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,Register_Page_Link, {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect(admin)
            elif user is not None and user.is_citizen:
                login(request, user)
                return redirect(Citizen)
            elif user is not None and user.is_committee:
                login(request, user)
                return redirect(Committee)
            elif user is not None and user.is_securityguard:
                login(request, user)
                return redirect(Security)
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, Login_Page_Link, {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def Citizen(request):
    return render(request,'Citizen.html')


def Committee(request):
    return render(request,'Committee.html')
    
def Security(request):
    return render(request,'security.html')