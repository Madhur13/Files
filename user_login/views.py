from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User
from .models import *

from cashback.tasks import SignupTask,mul

def login_view(request):
    next_page = request.GET.get('next',reverse('index'))
    if request.method == 'GET':
        return render(request, 'user_login/login.html')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(next_page)
                else:
                    return render(request,'user_login/login.html',{'message':'Disabled user'})
            else:
                return render(request,'user_login/login.html',{'message':'Invalid User'})
        else:
            return render(request,'user_login/login.html',{'message':'Invalid User'})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    

def signup(request):
    if request.method == 'GET':
        form  = SignupForm()
        return render(request, 'user_login/signup.html', {'form':form} )
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            referral = form.cleaned_data['referral']
            if referral:
                if Customer.objects.filter(referral_code__iexact=referral):
                    user = User.objects.create_user(username,email,password, first_name=firstname,last_name=lastname)
                    customer = Customer(user=user, phone=phone, balance=0, referral_code='REFER'+str(user.id), referee_code=referral)
                else:
                    return render(request, 'user_login/signup.html', {'form':form,'referral_error':'Invalid Referral Code!!'})
            else:
                user = User.objects.create_user(username,email,password, first_name=firstname,last_name=lastname)
                customer = Customer(user=user, phone=phone, balance=0, referral_code='REFER'+str(user.id))                   
            customer.save()
            SignupTask.delay(user.email)
            #mul.delay(2,5)
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'user_login/signup.html', {'form':form} )




