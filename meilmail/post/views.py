from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.http import HttpResponseForbidden

def writing(request):
    return render(request, 'writing.html')

def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.files = request.FILES['file']
        post.save() #쿼리셋 메소드입니다. 객체를 저장하도록 하는 메소드입니다.
        return redirect('/writing')
    return HttpResponseForbidden('allowed only via POST')