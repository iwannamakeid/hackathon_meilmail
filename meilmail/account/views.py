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

        # 로그인에 실패한 경우
        if user is None:
            messages.info(request, ": 회원이 아닙니다. 회원가입을 해주세요")
            return redirect('login')

        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        nickname = request.POST.get('nickname')
        
        # 입력 값이 비어있을 때
        if nickname == "" or email == "" or password == "":
            messages.info(request,"회원가입 정보를 모두 기입해주세요.")
            return redirect('signup')

        # 비밀번호가 다를 때
        if not password == password_confirm:
            messages.info(request, ": 비밀번호가 다릅니다.")
            return redirect('signup')
        
        # Validation 성공한 경우
        user = User.objects.create_user(username=email, password=password)
        account = Account(user=user, email=email, nickname=nickname)
        account.save()
        return redirect('login')
    else:
        return render(request, 'account/signup.html')