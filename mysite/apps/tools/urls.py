from django.conf.urls import include

from django.conf.urls import url
from .views import ticketleft_init_view, ticketleft_query_view, wechat_view

from django.urls import path

app_name = '[tools]'

urlpatterns = [
    path('ticketleft/init/', ticketleft_init_view, name='ticketleft_init_url'),
    path('ticketleft/query/', ticketleft_query_view, name='ticketleft_query_url'),
    path('wechat/', wechat_view, name='wechat_url'),

]
