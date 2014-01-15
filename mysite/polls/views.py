from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.models import User
import re
from django.shortcuts import HttpResponse
from django import template
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponseRedirect
from polls.models import Data

class ContactForm(forms.Form):
    email = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class ContactForm2(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

def lodin_users(email,nickname,password):
    try:
        user = User.objects.create_user(nickname, email, password)
        user.is_staff = True
        user.save()
        return True 
    except:
        return False   

def authenticate_users(username,password,request):
    user = authenticate(username=username, password=password)

    if user is not None:
        print user    
        if user.is_active:
            return True
        else:
            return False
    else:
        return False

def logout(request):
    auth.logout(request)
    return render(request, 'polls/index.html')

def index(request):
    return render(request, 'polls/index.html')

def login(request):
    return render(request, 'polls/login.html')

def signin(request):
    return render(request, 'polls/signin.html')

def get_info(request,offset):
    rlat = re.compile(r'lat=(-*\d+\.\d+)')
    lat= re.findall(rlat, offset)
    rlng = re.compile(r'lng=(-*\d+\.\d+)')
    lng= re.findall(rlng, offset)
    data=Data(lat[0],lng[0]) 
    twitts= data.get_twitts()
    insts= data.get_photos()
    return render(request, 'polls/get_info.html', {'tweets':twitts,'insts':insts})

def post_login(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            email = form.cleaned_data['email']
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']
            f=lodin_users(email,nickname,password)
            if f==True:
                return render(request, 'polls/success.html')
            else:
                return render(request, 'polls/fail.html')

def post_signin(request):

    if request.method == 'POST': 
        form = ContactForm2(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            f=authenticate_users(username,password,request)
            if f==True:
                return render(request, 'polls/map.html')
            else:
                return render(request, 'polls/signin.html')
