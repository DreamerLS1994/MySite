from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Catalogue
from django.shortcuts import get_object_or_404


# Create your views here.

def index_view(request):
    #return HttpResponse("Hello World! From Jerry Coding")
    articles = Article.objects.all()  # 获取所有文章数据
    catalogues = Catalogue.objects.all() # 获取所有分类数据

    return render(request, 'blog/index.html', {'article_list':articles, 'cata_list':catalogues}) #返回给index用于显示
    # return render(request, 'blog/index.html')

def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)  #获取该slug的文章
    return render(request,'blog/article_detail.html', {'article':article})   # 返回article_detail.html页面

def catalogue_view(request, slug):
    this_cata = get_object_or_404(Catalogue, slug=slug) #找到该目录
    articles = Article.objects.filter(catalogue = this_cata) # 找到属于该目录的所有文章
    catalogues = Catalogue.objects.all() # 获取所有分类数据

    return render(request, 'blog/cata_detail.html', {'article_list':articles, 'cata_list':catalogues})
 
