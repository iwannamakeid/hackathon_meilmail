from django.db import models

class Post(models.Model): #글 모델

    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField() # 혹시나 검색같은 경우에 쓰일까 싶어서 넣었습니다.
    body = models.TextField()
    files = models.FileField(upload_to='files/%Y%M', blank = True)

    def __str__(self):
        return self.title