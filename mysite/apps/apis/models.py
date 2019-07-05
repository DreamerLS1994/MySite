from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('分类名称', unique=True, max_length=20, help_text='分类名称，最多20个字符。')
    summary = models.CharField('分类介绍', max_length=255, help_text='垃圾分类介绍。最多255字符')

    class Meta:
        verbose_name = '垃圾分类'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name


class Rubbish(models.Model):
    name = models.CharField('垃圾名称', unique=True, max_length=20, help_text='垃圾名称，最多20个字符。')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', help_text='选择垃圾的分类')

    class Meta:
        verbose_name = '垃圾'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name
