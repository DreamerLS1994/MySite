
from django.conf.urls import url
from .views import index_view

from django.urls import path

app_name = '[blog]'

urlpatterns = [
   # url(r'^$', index_view, name='index_url'),
    path('', index_view, name='index_url'),
]
