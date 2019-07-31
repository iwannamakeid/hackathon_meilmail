from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils import timezone
from django.http import HttpResponseForbidden

def home(request):
    post_list = Post.objects.all() 
    return render(request, 'home.html', {'post_list':post_list})

def detail(request, post_id):
    post=Post.objects.get(id=post_id)
    comments = post.comment_set.all().order_by('-pub_date')
    return render(request,"detail.html", {'post':post, 'comments': comments})

def write(request):
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

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    # 각 글의 고유한 아이디를()에 넣어야함, id=는 변수, post_id=상수값. 
    post.delete()
    return redirect('home')

#어려운 부분: 갱신하기
def edit(request,post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('')       

    else:
        post=Post.objects.get(id=post_id)
        return render (request, 'edit.html',{"post": post})

def comment_create(request, post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        comment=Comment(post=post)
        # 파랑포스트는 models에 있는 변수 post, 흰 포스트는 객체의 값 특정된 것(엄마=엄마이름)
        comment.content=request.POST['content']
        comment.save()
        
        return redirect('detail',post_id)

