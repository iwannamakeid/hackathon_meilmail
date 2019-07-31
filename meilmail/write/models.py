from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now) # ('date published'): 작성날짜
    files = models.FileField(upload_to='files/%Y%M', blank = True)

    def __str__(self):
        return self.title
       


class Comment(models.Model):
    # 일대다 관걔 정해주는 방법(a와b는 종속적이다.)
    post=models.ForeignKey(Post, 
    on_delete=models.CASCADE)
    # 종속한모델이 없어졌을 때 종속된 것이 모두 사라짐
    content =models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        
        return self.content
    
    # class Meta:
    #     # comment.objects.all().order_by('date_joined') 
