from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import Article, Catalogue
from comment.models import Comment

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from django.shortcuts import get_object_or_404


# Create your views here.


def page_not_found(request, exception):
    # 刚刚创建的404.html  路径要写对
    response = render_to_response("blog/404.html", {})
    response.status_code = 404
    return response

'''
下面是处理服务器错误 500 的函数，少一个request 参数
def page_error(exception):
    response = render_to_response("blog/500.html", {})
    response.status_code = 500
    return response
'''

def index_view(request):
    #return HttpResponse("Hello World! From Jerry Coding")
    article_list = Article.objects.all()  # 获取所有文章数据
    catalogues = Catalogue.objects.all() # 获取所有分类数据
    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except InvalidPage:
        return HttpResponse('404NOT FOUND')
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'article_list':articles, 'cata_list':catalogues}) #返回给index用于显示
    # return render(request, 'blog/index.html')

def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)  #获取该slug的文章
    cmt_list = Comment.objects.filter(belong = article)  #获取该文章的所有评论
    return render(request,'blog/article_detail.html', {'article':article, 'cmt_list':cmt_list})   # 返回article_detail.html页面

def catalogue_view(request, slug):
    this_cata = get_object_or_404(Catalogue, slug=slug) #找到该目录
    article_list = Article.objects.filter(catalogue = this_cata) # 找到属于该目录的所有文章
    catalogues = Catalogue.objects.all() # 获取所有分类数据
    
    paginator = Paginator(article_list, 2,1)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except InvalidPage:
        return HttpResponse('404NOT FOUND')
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/cata_detail.html', {'article_list':articles, 'cata_list':catalogues})
 
