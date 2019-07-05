import xadmin
from xadmin import views
from .models import Rubbish, Category

class RubbishAdmin(object):
    # 菜单图标
    model_icon = 'fa fa-trash'
    # 分类筛选
    list_filter = ('category',)
    # 搜索框
    search_fields = ('name',)  # 指定要搜索的字段



class CategoryAdmin(object):
    # 菜单图标
    model_icon = 'fa fa-trash'
    pass


xadmin.site.register(Rubbish, RubbishAdmin)
xadmin.site.register(Category, CategoryAdmin)