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


# 测试 Model字段
class TestModel(models.Model):
        test2 = models.DateField(verbose_name='日期')
        test3 = models.DateTimeField(verbose_name='时间日期')
        # decimal_places 小数点位数 精度  max_digits 最大位数
        test4 = models.DecimalField(verbose_name='十进制小数', max_digits=10, decimal_places=5)
        test5 = models.FloatField(verbose_name='浮点数')
        test6 = models.IntegerField(verbose_name='整形')
        test7 = models.BigIntegerField(verbose_name='长整形')
        test8 = models.SmallIntegerField(verbose_name='Small INT')
        test9 = models.PositiveIntegerField(verbose_name='正数INT')
        test10 = models.PositiveSmallIntegerField(verbose_name='正数Small INT')
        '''
        范围取值：
　　　　'SmallIntegerField': (-32768, 32767),
　　　　'IntegerField': (-2147483648, 2147483647),
　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),
　　　　'PositiveSmallIntegerField': (0, 32767),
　　　　'PositiveIntegerField': (0, 2147483647),
        '''

        test12 = models.GenericIPAddressField(verbose_name='IP地址')
        test13 = models.SlugField(verbose_name='Slug')

        test14 = models.TextField(verbose_name='文本框')
        test15 = models.TimeField(verbose_name='时间')
        test16 = models.URLField(verbose_name='URL地址')
        test17 = models.BinaryField(verbose_name='二进制')
        test18 = models.ImageField(verbose_name='图片')
        test19 = models.FileField(verbose_name='文件')

        class Meta:
                verbose_name = '测试Model'  # 通俗易懂的名字
                verbose_name_plural = verbose_name  # 复数形式

        def __str__(self):
                return "测试Model"
