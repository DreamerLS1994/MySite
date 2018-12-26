from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 文章分类model
class Catalogue(models.Model):
        name = models.CharField('分类名称', max_length=20)
        slug = models.SlugField('唯一标识', unique=True, default='cata_slug_default(请修改)')
        disc = models.TextField('分类介绍', max_length=300, default='请输入该分类的介绍....')

        class Meta:
                verbose_name = '文章分类'
                verbose_name_plural = verbose_name
                ordering=['name']

        def __str__(self):
                return self.name


# 文章model
class Article(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='作者')
        title = models.CharField(max_length=150, verbose_name='标题')
        summary = models.TextField('摘要', max_length=300, default='请输入文章摘要....')
        # body = models.TextField(verbose_name='内容', default='请输入文章内容....')
        body = RichTextUploadingField(verbose_name='内容', default='请输入文章内容....')
        create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
	
	#slug 。这个其实就是用在文章的URL的。
	#比如你现在一篇文章的标题是“i like django”,你可以把slug设置成"i-like-django",然后显示在浏览器的地址URL就是比如这样www.example.com/article/i-like-django/
	#因为每个文章都是唯一的，这个slug也一定要唯一，所以你在里面设置的参数是unique=True。    
        slug = models.SlugField('唯一标识', unique=True, max_length=20, default='slug_input_default(请修改)')
        catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE, verbose_name='文章分类')

        class Meta:
                verbose_name = '文章'                  #通俗易懂的名字
                verbose_name_plural = verbose_name      # 复数形式
                ordering=['-create_date']               # 降序排序

        def __str__(self):
                return self.title[:20]

