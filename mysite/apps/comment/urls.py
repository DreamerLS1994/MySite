from django.urls import path
from .views import cmt_add_view, msg_all_view, msg_unread_view

app_name = '[comment]'

urlpatterns = [
    path('add/',cmt_add_view, name='cmt_add_url'),  # 添加评论:
    path('message/all',msg_all_view, name='msg_all_url'),  # 所有消息
    path('message/unread',msg_unread_view, name='msg_unread_url'),  # 未读消息
]

