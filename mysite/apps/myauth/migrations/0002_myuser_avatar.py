# Generated by Django 2.1.4 on 2018-12-23 15:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatar/default.png', upload_to='avatar', verbose_name='头像'),
        ),
    ]
