from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Article
from .models import Comment, Message

# Create your views here.

@login_required
@require_POST
def cmt_add_view(request):
    if request.is_ajax():
        cmt_user = request.user                       #获取评论的用户
        cmt_articleid = request.POST.get('article_id')     #获取评论的文章
        cmt_body = request.POST.get('body')                #获取评论的内容

        article = Article.objects.get(id=cmt_articleid)     #获取评论的文章

        comment = Comment(owner=cmt_user, body=cmt_body, belong=article)  #创建一个新的comment

        comment.save()            #保存数据

        return JsonResponse({'msg':'评论提交成功！'})
    return JsonResponse({'msg':'评论提交失败！'})

@login_required
def msg_all_view(request):
    msg_list = Message.objects.filter(receiver = request.user)
    return render(request, 'comment/msg_list.html',{'msg_list':msg_list})



@login_required
def msg_unread_view(request):
    msg_list = Message.objects.filter(receiver = request.user)
    msg_list2 = []
    for msg in msg_list:
        if msg.is_read == False:
            msg_list2.append(msg)

    return render(request, 'comment/msg_list.html',{'msg_list':msg_list2})

@receiver(post_save, sender=Comment)
def create_msg_handler(sender, instance, **kwargs):
    article = instance.belong   # instance 就是发信号的对象，这里是个评论
    sender = instance.owner     # 获取评论者，即消息发送者
    receiver = article.author   # 通知文章作者
    msg = Message(sender=sender, receiver=receiver, belong=instance)  # 新建消息保存
    msg.save()



    

