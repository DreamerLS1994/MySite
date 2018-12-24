from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Myuser(AbstractUser):
    # 添加头像
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 #图片将处理成100 x 100的尺寸
                                 processors=[ResizeToFill(100,100)],)

    # 添加个性签名字段
    signature = models.CharField(max_length=50, blank=True, null=True, verbose_name="签名")
    
    def __str__(self):
        return self.username


