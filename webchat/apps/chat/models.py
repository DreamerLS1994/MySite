from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('username',max_length=20, unique=True)
    password = models.CharField('password',max_length=20)

    state = models.CharField('state', max_length=10)
    friend = models.ManyToManyField('self', verbose_name='friend')
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
