
from django.conf.urls import url
from .views import index_view

from django.urls import path

app_name = '[blog]'

urlpatterns = [
    path('', index_view, name='index_url'),
]
