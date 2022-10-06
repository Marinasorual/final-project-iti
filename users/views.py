from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, render
from django.contrib.auth import authenticate, login, logout as logoutUser
from django.contrib.auth.models import User
from django.contrib import messages

from blog.models import Category


# Create your views here.



def showLogin(request):
    return render(request,'login.html')



def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active == True :
        login(request, user)
        return redirect('/')
    else:
        # Return an 'invalid login' error message.
        messages.warning(request, 'Your account in locked, please contact admin')
        return HttpResponseRedirect('/login')
        return HttpResponse(request.user.username)

def showRegister(request):
    return render(request,'register.html')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password_confirm = request.POST['password_confirmation']

    if password == password_confirm:
        user = User.objects.create_user(username, email, password)
        return redirect('/')
    else:
        return redirect('/register');

def logout(request):

    logoutUser(request)

    return  HttpResponseRedirect('/')

def categorySubscribe(request,id):
    category = Category.objects.get(pk=id)
    user = request.user

    category.user.add(user)

    return HttpResponseRedirect('/')

def categoryUnSubscribe(request,id):
    category = Category.objects.get(pk=id)
    user = request.user
    category.user.remove(user)

    return HttpResponseRedirect('/')