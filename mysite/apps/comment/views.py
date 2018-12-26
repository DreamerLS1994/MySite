from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from blog.models import Article
from .models import Comment

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

