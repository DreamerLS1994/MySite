# Generated by Django 2.1.4 on 2018-12-25 11:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='请输入文章内容....', verbose_name='内容'),
        ),
    ]
