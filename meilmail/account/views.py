from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Account

# Create your views here.

def home(request):
    return render(request, 'account/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, ": 회원이 아닙니다. 회원가입을 해주세요")
            return redirect('login')
        return redirect('home')
    else:
        render(request, 'account/login.html')

    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        nickname = request.POST.get('nickname')
        print(nickname)
        if nickname != "" and email != "" and password != "":
            if password == password_confirm:
                user = User.objects.create_user(
                    username=email,
                    password=password
                )
                account = Account()
                account.user = user
                account.email = email
                account.nickname = request.POST.get('nickname')
                account.save()
                return redirect('login')
            else:
                messages.info(request, ": 비밀번호가 다릅니다.")
                return redirect('signup')
        else:
            messages.info(request,"회원가입 정보를 모두 기입해주세요.")
            return redirect('signup')
        
    else:
        return render(request, 'account/signup.html')