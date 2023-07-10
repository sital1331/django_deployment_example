from django.shortcuts import render
from django.http import HttpResponse
from learning_users.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"learning_users/index.html")
def register(request):
    registered= False

    if(request.method=='POST'):
        user_form= UserForm(data=request.POST)
        user_info_form= UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile= user_info_form.save(commit=False)
            profile.user=user
        
            if 'portfolio_pic' in request.FILES:
                profile.portfolio_pic=request.FILES['portfolio_pic']

            profile.save()

            registered= True
        else:
            print(user_form.errors,user_info_form.errors)
    else:
        
        user_form= UserForm()
        user_info_form = UserProfileInfoForm()

    return render(request,"learning_users/register.html",
                      {'user_form':user_form,'user_info_form':user_info_form,'registered':registered})

def user_login(request):

    if request.method=="POST":
        user_name = request.POST.get('username')
        pswd = request.POST.get('password')

        user= authenticate(username=user_name,password=pswd)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,"learning_users/index.html")
            else:
                return HttpResponse("Account not active")
        else:
            print("Login Failed!!")
    else:
        return render(request,"learning_users/user_login.html")
    
@login_required
def user_logout(request):
    logout(request)
    return render(request,"learning_users/index.html")
