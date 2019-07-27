from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    # 장고 유저와 내가 만든 모델 1대1 연결
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username