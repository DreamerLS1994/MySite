# Generated by Django 2.1.4 on 2018-12-27 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='is read or not')),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_messages', to='comment.Comment', verbose_name='belong')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_message', to=settings.AUTH_USER_MODEL, verbose_name='receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_message', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Message',
                'ordering': ['-create_date'],
            },
        ),
    ]