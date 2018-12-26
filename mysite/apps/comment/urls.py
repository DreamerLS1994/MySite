

from django.urls import path
from .views import cmt_add_view

app_name = '[comment]'

urlpatterns = [
    path('add/',cmt_add_view, name='cmt_add_url'),  # 添加评论:
]

