from django.contrib import admin
from blog.models import Article, Catalogue

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'author','body','id'] # 显示列表项
    list_filter = ('author',) # 过滤器
        
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
        list_display = ['name', 'disc', 'id']

