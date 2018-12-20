from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Myuser(AbstractUser):
    # 添加个性签名字段
    signature = models.CharField(max_length=50, blank=True, null=True, verbose_name="签名")

    def __str__(self):
        return self.username


