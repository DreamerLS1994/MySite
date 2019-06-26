from django.contrib import admin
from blog.models import Article, Catalogue

import xadmin
from xadmin import views

class GlobalSetting(object):
    # 设置后台顶部标题   
    site_title ='博客后台管理'
    # 设置后台底部标题   
    site_footer ='博客后台管理'


class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True
    # 使用主题   
    use_bootswatch = True


class ArticleAdmin(object):
    # 菜单图标
    model_icon = 'fa fa-book'
    # 分类筛选
    list_filter = ('catalogue',)
    # 搜索框
    search_fields = ('title',)  # 指定要搜索的字段

    # 图表显示
    data_charts = {
        "user_count": {'title': u"统计", "x-field": "id", "y-field": "create_date", "order": ('create_date',)},
    }


# 标题栏
xadmin.site.register(views.CommAdminView, GlobalSetting)
# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Article, ArticleAdmin)

'''
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'author','body','id'] # 显示列表项
    list_filter = ('author',) # 过滤器
        
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
        list_display = ['name', 'disc', 'id']
'''
