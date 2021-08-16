from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as login_page ,logout as logout_page

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method =="POST":  
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1==password2:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login_page(request,user)
                return redirect('home')
        return render (request,'accounts/signup.html')
