from django.db import models
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='评论人')
    body = models.TextField('评论内容')
    create_date = models.DateTimeField('评论时间', auto_now_add=True)

    belong = models.ForeignKey(settings.ARTICLE_MODEL, on_delete=models.CASCADE, related_name='articles_comments', verbose_name='所属文章')


    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['create_date']

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender_message', verbose_name='发送者')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message', verbose_name='接收者')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    is_read = models.BooleanField('是否已读', default = False)

    belong = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_messages', verbose_name='所属评论')

    class Meta:
        verbose_name = '消息通知'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']
    
    def mark_read(self):
        self.is_read = True
        self.save(update_fields=['is_read'])
